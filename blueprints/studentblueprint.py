from flask import Blueprint, request, render_template
from controller.student_addcontroller import add_student

student_blueprint = Blueprint('student', __name__)

@student_blueprint.route('/register-student', methods=['POST'])
def add_student_route():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        schoolname = request.form['schoolname']
        emailid = request.form['emailid']
        mobileno = request.form['mobileno']
        sex = request.form['sex']
        address= request.form['address']
        saved_details= add_student(name, course ,schoolname ,emailid , mobileno, sex, address)

        #Give template?
        return 'Student added successfully.'
    return render_template('add_student.html')