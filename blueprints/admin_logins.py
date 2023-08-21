from flask import Blueprint, request, render_template
from config import Client
import datetime

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



@admin_blueprint.route('/make_announcement', methods=['POST'])
def ul_make_announcement():
    if request.method == "POST":
        return render_template("university/make_announcement.html")

@admin_blueprint.route('/submit-announcement', methods= ['POST'])
def submit_announcement():
    if request.method == "POST":
        current_timestamp = datetime.datetime.now()
        current_date = current_timestamp.date()
        current_time = current_timestamp.time()
        formatted_date = current_date.strftime('%Y-%m-%d')
        formatted_time = current_time.strftime('%H:%M:%S')

        title= request.form['title']
        description= request.form['description']
        db = Client["studentdata"]

        # Choose the collection
        collection = db["Admin_announcement"]

        announcement_json= {'title': title, 'description': description, 'timestamp': formatted_date + ' ;' + formatted_time}
        collection.insert_one(announcement_json)
        announcements = collection.find()
        print(announcements)
        return '<h4> Thanks the announcement has been made '

@admin_blueprint.route('/view_announcement', methods= ['GET'])
def view_announcement():


    db = Client["studentdata"]
    collection = db["Admin_announcement"]
    announcements = list( collection.find())

    return render_template('university/view_announcement.html',data= announcements)

