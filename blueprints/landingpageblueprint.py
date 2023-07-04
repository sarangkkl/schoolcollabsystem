from flask import Blueprint, request, render_template
import hashlib
from config import Client


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
                return None

        name= get_student_by_name(name)
        print(name)

        stored_password = name['password']

        print("Stored Password:", stored_password)

        if stored_password == password:
            return "True"
        else:
            return "False"

        #After sign in show him dashboards


    else:
        return render_template('scs.html')