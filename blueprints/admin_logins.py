from flask import Blueprint, request, render_template, redirect, url_for
from config import Client
import datetime
from werkzeug.utils import secure_filename
from gridfs import GridFS

import bson,json, os
from config import PATH

UL_ADMIN_CODE = '123456'
DCU_ADMIN_CODE= '654321'

admin_blueprint = Blueprint('adminlogin', __name__)

@admin_blueprint.route('/admindash', methods=['GET'])
def admin_login():
    return render_template("adminlogin/adminlogin.html")

@admin_blueprint.route('/ul_login_dash', methods=['GET'])
def ul_login_dash():
    return render_template("adminlogin/ul_admin.html")

@admin_blueprint.route('/dcu_login_dash', methods=['POST'])
def dcu_login_dash():
    if request.method == "POST":
        print('dcu')
        if request.form['code'] == '654321':
            return render_template("adminlogin/dcu-admin-dash.html")


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

@admin_blueprint.route('/make_meetings', methods= ['POST'])
def make_meeting():
    if request.method == 'POST':
        return render_template('university/make_meeting.html')

@admin_blueprint.route('/create_meetings', methods= ['POST'])
def create_meeting():
    title= request.form['title']
    meeting_link= request.form['meeting_link']
    db = Client["studentdata"]
    collection = db["Admin_meetings"]
    json_data= {'title': title, 'meeting_link': meeting_link}
    collection.insert_one(json_data)
    return '<h4> Thanks the meeting has been made '

@admin_blueprint.route('/view_meetings', methods= ['GET'])
def view_meeting():
    db = Client["studentdata"]
    collection = db["Admin_meetings"]
    meetings = list(collection.find())
    return render_template('university/view_meetings.html',data= meetings)


@admin_blueprint.route('/share_links', methods= ['POST'])
def share_links():
    if request.method == "POST":
        return render_template('university/make_share_link.html')

@admin_blueprint.route('/share_link_post', methods= ['POST'])
def share_link_post():
    if request.method == "POST":
        title = request.form['title']
        link = request.form['link']
        db = Client["studentdata"]
        collection = db["Admin_sharelink"]
        json_data = {'title': title, 'link': link}
        collection.insert_one(json_data)
        return '<h4> Thanks the link has been shared '

@admin_blueprint.route('/view_link_post', methods= ['GET'])
def view_link_post():
    db = Client["studentdata"]
    collection = db["Admin_sharelink"]
    links = list(collection.find())
    return render_template('university/view_shared_links.html', data= links)



@admin_blueprint.route('/share_resources', methods= ['POST'])
def share_resources():
    if request.method == "POST":
        return render_template('university/make_share_resource.html')


@admin_blueprint.route('/post_shared_resources', methods= ['POST'])
def share_resources_post():
    if request.method == 'POST':

        from schoolapp import app
        from config import PATH
        app.config['UPLOAD_FOLDER'] = PATH
        UPLOAD_FOLDER = '/path/to/upload/folder'
        ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx', 'doc'}

        db = Client["studentdata"]
        file = request.files['file']

        def allowed_file(filename):
            return '.' in filename and \
                   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return 'File uploaded successfully'
        else:
            return 'Invalid file format or no file provided'

@admin_blueprint.route('/view_shared_resources', methods=['GET', 'POST'])
def view_shared_resources():
    if request.method == "POST":
        # Handle POST requests as needed
        pass
    else:
        files = os.listdir(r'C:/Users/Tejas Jagannatha/PycharmProjects/schoolcollab_Dissertation/shared_resources')
        return render_template('university/view_shared_resources.html', files=files)
