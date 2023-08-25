from flask import Blueprint, request, render_template

university_blueprint = Blueprint('university', __name__)
@university_blueprint.route('/university', methods=['POST'])
def ul_display():
    if request.method == "POST":
        #Ul dashboard
        if request.form['university'] == "ul":
            return render_template("university/Ul_landingpage.html")
            print("UL")
            pass

        #Dcu dashboard
        elif request.form['university'] == "dcu":
            print("DCU")
            return render_template("adminlogin/dcu-admin-dash.html")


