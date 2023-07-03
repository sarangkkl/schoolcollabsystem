from flask import Blueprint, request, render_template
landingPage_blueprint = Blueprint('landingpage', __name__)

@landingPage_blueprint.route('/SCS', methods=['GET', 'POST'])
def landingpage_route():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        #After sign in show him dashboards

    else:
        return render_template('scs.html')