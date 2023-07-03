# A class for student who would register
from config import Client
import bcrypt


class Student:
    def __init__(self, name, password, course, schoolname, emailid, mobileno, sex, address):
        self.name = name
        self.password = password
        self.course = course
        self.schoolname = schoolname
        self.emailid = emailid
        self.mobileno = mobileno
        self.sex = sex
        self.address = address

    def save(self):
        # Code to save the student to a database or any other storage
        db_newstudent = Client["studentdata"]
        registered_student = db_newstudent["registeredstudents"]

        registered_student_data = {
            "name": self.name,
            "password": self.password,
            "course": self.course,
            "schoolname": self.schoolname,
            "emailid": self.emailid,
            "mobileno": self.mobileno,
            "sex": self.sex,
            "address": self.address
        }

        registered_student.insert_one(registered_student_data)  # Insert the student data into the collection

    def get_student_data(self):
        db_student = Client["studentdata"]
        registered_student = db_student["registeredstudents"]
        try:
            filter = {
                'emailid': {'$eq': self.emailid},
            }

            # Execute the query
            result = list(registered_student.find(filter, {'_id': 0}))[0]

            return result

        except:
            return None

