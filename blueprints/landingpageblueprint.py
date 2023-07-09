from flask import Blueprint, request, render_template, session
import hashlib
from config import Client
from passlib.hash import sha256_crypt
from flask_mail import Mail, Message
import pyotp
from MFA import generate_otp

landingPage_blueprint = Blueprint('landingpage', __name__)

@landingPage_blueprint.route('/SCS', methods=['GET', 'POST'])
def landingpage_route():
    if request.method == "POST":
        name = request.form['username']
        password = request.form['password']

        db_newstudent = Client["studentdata"]
        registered_student = db_newstudent["registeredstudents"]

        #Gets student details using name
        def get_student_by_name(name):
            try:
                filter = {
                    'name': name,
                }
                # Execute the query
                result = registered_student.find_one(filter, {'_id': 0})
                return result
            except:
                #Handle HTTP No data found
                return None

        resultname= get_student_by_name(name)

        print(resultname)
        stored_password = resultname['password']
        stored_emailid= resultname['emailid']

        # Hash the entered password using the same algorithm and encoding as the stored password
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        hashed_password = sha256_hash.hexdigest()



        if hashed_password == stored_password:
            from schoolapp import app
            mail = Mail(app)
            msg = Message('Here is your Code', sender='tejasjagannatha@gmail.com', recipients=[stored_emailid])

            secret_key = generate_otp.generate_otp()
            print("landing page",secret_key)
            msg.html = render_template('mailingsystem/sendotp.html', code=secret_key)
            mail.send(msg)
            session['token'] = secret_key
            return render_template('mfa_check.html', emailid= stored_emailid)


        else:
            return 'Invalid password'

        #After sign in show him dashboards


    else:
        return render_template('scs.html')