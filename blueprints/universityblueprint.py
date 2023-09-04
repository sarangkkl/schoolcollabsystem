from flask import Blueprint, request, render_template

university_blueprint = Blueprint('university', __name__)
@university_blueprint.route('/university', methods=['POST'])
def ul_display():
    if request.method == "POST":
        #Ul dashboard
        if request.form['university'] == "ul":
<<<<<<< HEAD

            return render_template("university/Ul_landingpage.html")

=======
            return render_template("adminlogin/ul_admin.html")
            print("UL")
            pass
>>>>>>> 'testing-OTPfeature'

        #Dcu dashboard
        elif request.form['university'] == "dcu":
            print("DCU")
<<<<<<< HEAD
            return render_template("university/DCU_USER_DASH.html")
=======
            return render_template("adminlogin/dcu_admin.html")
>>>>>>> 'testing-OTPfeature'


