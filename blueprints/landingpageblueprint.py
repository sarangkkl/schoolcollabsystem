from flask import Blueprint, request, render_template, session
import hashlib
from config import Client
from passlib.hash import sha256_crypt
from flask_mail import Mail, Message
import pyotp,time
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
        if resultname:
            stored_password = resultname['password']
            stored_emailid= resultname['emailid']

            # Hash the entered password using the same algorithm and encoding as the stored password
            sha256_hash = hashlib.sha256()
            sha256_hash.update(password.encode('utf-8'))
            hashed_password = sha256_hash.hexdigest()
            valid = 0

            if hashed_password == stored_password:
                from schoolapp import app
                mail = Mail(app)
                msg = Message('Here is your Code', sender='tejasjagannatha@gmail.com', recipients=[stored_emailid])
                key_obj, key_val = generate_otp.generate_otp()
                msg.html = render_template('mailingsystem/sendotp.html', code=key_val)
                mail.send(msg)
                session['token'] = key_obj
                print("Key obj: ",key_obj)
                valid= 1
                print('valid')

                return render_template('mfa_check.html', emailid= stored_emailid, isvalid= valid)

            else:
                valid = 0
                print('Invalid')
                return render_template('mfa_check.html', emailid=None, isvalid=valid)

        else:
            valid= 0
            return render_template('mfa_check.html', emailid= None, isvalid=valid)

    else:
        return render_template('scs.html')


@landingPage_blueprint.route('/resetuser', methods=['POST', 'GET'])
# Reset password
def reset_user():
    print('as')
    if request.method == "POST":
        email= request.form['regid']

        db_newstudent = Client["studentdata"]
        registered_student = db_newstudent["registeredstudents"]


        # Gets student details using name
        def get_student_byemail(email):
            try:
                filter = {
                    'emailid': email,
                }
                # Execute the query
                result = registered_student.find_one(filter, {'_id': 0})
                print(result)
                return result
            except:
                # Handle HTTP No data found
                return None
        result= get_student_byemail(email)
        if result:
            #your username is this
            session['password'] = result['password']
            session['name'] = result['name']

            print( result['password'])

            #Change password?
            return render_template('passwordreset.html', password= result['password'], name= result['name'])

        #if email data is not found
        else:
            return render_template('email_notfound.html')
    else:
        return render_template('resetuser.html')


@landingPage_blueprint.route('/changepassword', methods=['POST', 'GET'])
# Reset password
def change_password():
    if request.method == "POST":
        print('post')
        # Change request for password
        existing_pass= session.get('password')
        username= session.get('name')

        new_pass= request.form['password']
        print(new_pass)
        db_newstudent = Client["studentdata"]
        registered_student = db_newstudent["registeredstudents"]
        # Hash the entered password using the same algorithm and encoding as the stored password
        sha256_hash = hashlib.sha256()
        sha256_hash.update(new_pass.encode('utf-8'))
        hashed_password = sha256_hash.hexdigest()
        myquery = {"name": username}
        newvalues = {"$set": {"password": hashed_password}  }
        registered_student.update_one(myquery, newvalues)

        #Successful Password changed
        return render_template('password_change_successful.html')
