from flask import Blueprint, request, render_template

university_blueprint = Blueprint('university', __name__)
@university_blueprint.route('/university', methods=['POST'])
def ul_display():
    if request.method == "POST":
        #Ul dashboard
        if request.form['university'] == "ul":

            return render_template("university/Ul_landingpage.html")


        #Dcu dashboard
        elif request.form['university'] == "dcu":
            print("DCU")
            return render_template("university/DCU_USER_DASH.html")


