""" Student Profile dashboards visible after MFA """
from flask import Blueprint, request, render_template,session
from MFA import generate_otp
import pyotp


dashboard_blueprint = Blueprint('dashboard', __name__)


@dashboard_blueprint.route('/dashboard', methods=['POST'])
def dashboard_route():
    if request.method == "POST":

        secret_key = session.get('token')

        user_code = request.form['token']
        totp = pyotp.TOTP(secret_key)
        print("Secret Key:", secret_key)
        print("User Code:", user_code)
        is_valid = totp.verify(user_code)
        print("Is Valid:", is_valid)



