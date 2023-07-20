""" Student Profile dashboards visible after MFA """
from flask import Blueprint, request, render_template,session
from MFA import generate_otp
import pyotp, time
from pyotp import TOTP

dashboard_blueprint = Blueprint('dashboard', __name__)


@dashboard_blueprint.route('/dashboard', methods=['POST'])
def dashboard_route():
    if request.method == "POST":

        user_code = request.form['token']
        otp= TOTP(session['token'])
        isvalid= otp.verify(user_code,valid_window=1)
        #check if user entered right OTP
        if isvalid:
            return render_template('dashboard.html')


        else:
            return "Invalid Code or Code expired (30 seconds time to enter code)"

