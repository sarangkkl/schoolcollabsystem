from flask import Blueprint, request, render_template, session
import hashlib
import pika
from config import Client
from passlib.hash import sha256_crypt
from flask_mail import Mail, Message
import pyotp, time, threading
from MFA import generate_otp

def producer(message):
    rabbitmq_url = "amqps://bdpjerhx:YWZPuQON6FmFnlkw__aghPSdKEPy16HC@cougar.rmq.cloudamqp.com/bdpjerhx"

    connection_parameters = pika.URLParameters(rabbitmq_url)
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue='login')
    channel.basic_publish(exchange='', routing_key='login', body=message)
    connection.close()


def consumer(connection_parameters):
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue='login')

    def on_message_received(ch, method, properties, body):
        print("Message:", body)
        # Process the message here
        ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message

    channel.basic_consume(queue='login', on_message_callback=on_message_received)
    channel.start_consuming()


def consume_single_message(channel):
    queue_name = 'login'
    method_frame, header_frame, body = channel.basic_get(queue=queue_name)

    if method_frame:
        print("Received message:", body)
        # Process the message here

        # Acknowledge the message
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    else:
        print("No message in the queue.")


landingPage_blueprint = Blueprint('landingpage', __name__)


@landingPage_blueprint.route('/SCS', methods=['GET', 'POST'])
def landingpage_route():
    if request.method == "POST":
        name = request.form['username']
        password = request.form['password']
        db_newstudent = Client["studentdata"]
        registered_student = db_newstudent["registeredstudents"]

        def get_student_by_name(name):
            filter = {'name': name}
            result = registered_student.find_one(filter, {'_id': 0})
            return result

        resultname = get_student_by_name(name)

        if resultname:
            stored_password = resultname['password']
            stored_emailid = resultname['emailid']
            sha256_hash = hashlib.sha256()
            sha256_hash.update(password.encode('utf-8'))
            hashed_password = sha256_hash.hexdigest()

            if hashed_password == stored_password:
                from schoolapp import app
                mail = Mail(app)
                msg = Message('Here is your Code', sender='tejasjagannatha@gmail.com', recipients=[stored_emailid])
                key_obj, key_val = generate_otp.generate_otp()
                msg.html = render_template('mailingsystem/sendotp.html', code=key_val)
                mail.send(msg)
                session['token'] = key_obj
                valid = 1
                producer(stored_emailid)
                return render_template('mfa_check.html', emailid=stored_emailid, isvalid=valid)
            else:
                valid = 0
                producer(stored_emailid)
                return render_template('mfa_check.html', emailid=None, isvalid=valid)
        else:
            valid = 0
            return render_template('mfa_check.html', emailid=None, isvalid=valid)
    else:
        return render_template('scs.html')


@landingPage_blueprint.route('/resetuser', methods=['POST', 'GET'])
def reset_user():
    if request.method == "POST":
        email = request.form['regid']
        db_newstudent = Client["studentdata"]
        registered_student = db_newstudent["registeredstudents"]

        def get_student_by_email(email):
            filter = {'emailid': email}
            result = registered_student.find_one(filter, {'_id': 0})
            return result

        result = get_student_by_email(email)

        if result:
            session['password'] = result['password']
            session['name'] = result['name']
            return render_template('passwordreset.html', password=result['password'], name=result['name'])
        else:
            return render_template('email_notfound.html')
    else:
        return render_template('resetuser.html')


@landingPage_blueprint.route('/changepassword', methods=['POST', 'GET'])
def change_password():
    if request.method == "POST":
        existing_pass = session.get('password')
        username = session.get('name')
        new_pass = request.form['password']
        db_newstudent = Client["studentdata"]
        registered_student = db_newstudent["registeredstudents"]
        sha256_hash = hashlib.sha256()
        sha256_hash.update(new_pass.encode('utf-8'))
        hashed_password = sha256_hash.hexdigest()
        myquery = {"name": username}
        newvalues = {"$set": {"password": hashed_password}}
        registered_student.update_one(myquery, newvalues)
        return render_template('password_change_successful.html')

