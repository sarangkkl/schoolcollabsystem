from flask import Blueprint, request, render_template

UL_ADMIN_CODE = '123456'
DCU_ADMIN_CODE= '654321'

admin_blueprint = Blueprint('adminlogin', __name__)
@admin_blueprint.route('/admindash', methods=['GET'])
def admin_login():
    return render_template("adminlogin/adminlogin.html")

@admin_blueprint.route('/ul_login_dash', methods=['GET'])
def ul_login_dash():
    return render_template("adminlogin/ul_admin.html")

@admin_blueprint.route('/dcu_login_dash', methods=['GET'])
def dcu_login_dash():
    return render_template("adminlogin/dcu_admin.html")

@admin_blueprint.route('/ul-login', methods=['POST'])
def ul_login_admin():
    if request.method == "POST":
        if request.form['code'] == "123456":
            return render_template("adminlogin/ul-admin-dash.html")



@admin_blueprint.route('/ul-makeannouncement', methods=['POST'])
def ul_make_announcement():
    if request.method == "POST":
        print("ULLLLLLL")
        return render_template("university/make_announcement.html")
    pass
