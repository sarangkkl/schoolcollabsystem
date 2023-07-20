from flask import Blueprint, request, render_template
from controller.student_addcontroller import add_student
import hashlib

student_blueprint = Blueprint('student', __name__)
@student_blueprint.route('/register-student', methods=['POST', 'GET'])
def add_student_route(Message=None):
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        # Hash the entered password using the same algorithm and encoding as the stored password
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        hashed_password = sha256_hash.hexdigest()

        print("Entered Passw: ", password)
        print("Hashed Passw: " , hashed_password
              )
        course = request.form['course']
        schoolname = request.form['schoolname']
        emailid = request.form['emailid']
        mobileno = request.form['mobileno']
        sex = request.form.get('dropdown')
        address = request.form['address']

        saved_details = add_student(name, hashed_password, course, schoolname, emailid, mobileno, sex, address)
        from flask_mail import Mail, Message

        # Sends mail to the student
        def send_mail(emailid):
            from schoolapp import app
            mail = Mail(app)
            msg = Message('Thanks for joining us!', sender='tejasjagannatha@gmail.com', recipients=[emailid])
            msg.html = render_template('/mailingsystem/confirmationmail.html',name=name )

            #To handle fake emailadresses
            try:
                mail.send(msg)
            except:
                return render_template('mailingsystem/welcome.html')

        #call
        send_mail(emailid)

        return render_template('mailingsystem/welcome.html')

    return render_template('add_student.html')
