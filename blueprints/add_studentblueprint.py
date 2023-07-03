from flask import Blueprint, request, render_template
from controller.student_addcontroller import add_student

student_blueprint = Blueprint('student', __name__)
@student_blueprint.route('/register-student', methods=['POST', 'GET'])
def add_student_route(Message=None):
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        course = request.form['course']
        schoolname = request.form['schoolname']
        emailid = request.form['emailid']
        mobileno = request.form['mobileno']
        sex = request.form.get('dropdown')
        address = request.form['address']
        saved_details = add_student(name, password, course, schoolname, emailid, mobileno, sex, address)
        from flask_mail import Mail, Message

        # Sends mail to the student
        def send_mail(emailid):
            from schoolapp import app
            mail = Mail(app)
            msg = Message('Thanks for joining us!', sender='tejasjagannatha@gmail.com', recipients=[emailid])
            msg.html = render_template('/mailingsystem/confirmationmail.html')
            mail.send(msg)
        #call
        send_mail(emailid)

        return render_template('mailingsystem/welcome.html')

    return render_template('add_student.html')
