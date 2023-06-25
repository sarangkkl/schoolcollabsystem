from flask import Blueprint, request, render_template
landingPage_blueprint = Blueprint('landingpage', __name__)

@landingPage_blueprint.route('/SCS', methods=['GET'])
def landingpage_route():
    return render_template('landing_page.html')