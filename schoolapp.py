from flask import Flask, request, render_template
from controller.student_addcontroller import add_student

from flask import Flask
from blueprints.studentblueprint import student_blueprint

app = Flask(__name__)
app.register_blueprint(student_blueprint, url_prefix='/student')

if __name__ == '__main__':
    app.run()