from flask import Flask
from blueprints.add_studentblueprint import student_blueprint
from blueprints.landingpageblueprint import landingPage_blueprint
from blueprints.studentprofileblueprint import dashboard_blueprint
from blueprints.universityblueprint import university_blueprint
from blueprints.admin_logins import admin_blueprint
from flask_mail import Mail
from config import Client

#--- Flask Setup --#
app = Flask(__name__)

app.register_blueprint(student_blueprint)
app.register_blueprint(landingPage_blueprint)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(university_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='')

#--- Config controls ---#
app.static_folder = 'static'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tejasjagannatha@gmail.com'
app.config['MAIL_PASSWORD'] = 'jvobkcyyfarnkmtq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#-- Config sessions -- #
app.config['SECRET_KEY'] = '/t-_"8]Bg:u?RP87!aGW&VrLxq!t&V[C'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

    # Close the MongoDB connection always outside the function
    Client.close()
