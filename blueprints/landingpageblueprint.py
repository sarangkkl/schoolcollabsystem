from flask import Blueprint, request, render_template
import hashlib
from config import Client
from passlib.hash import sha256_crypt

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
        stored_password = resultname['password']

        # Hash the entered password using the same algorithm and encoding as the stored password
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        hashed_password = sha256_hash.hexdigest()

        if hashed_password == stored_password:
            return 'Login successful'

        else:
            return 'Invalid password'

        #After sign in show him dashboards


    else:
        return render_template('scs.html')