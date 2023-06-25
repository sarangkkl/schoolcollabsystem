# A class for student who would register
from config import URI_CONNECTION

class Student:
    def __init__(self, name ,course ,schoolname ,emailid , mobileno, sex, address):
        self.name= name
        self.course= course
        self.schoolname= schoolname
        self.emailid= emailid
        self.mobileno= mobileno
        self.sex= sex
        self.address = address


    def save(self):
        # Code to save the student to a database or any other storage
        db_newstudent = URI_CONNECTION["studentdata"]
        registered_student = db_newstudent["registeredstudents"]

        registered_student_data = {
            "name": self.name,
            "course": self.course,
            "schoolname": self.schoolname,
            "emailid": self.emailid,
            "mobileno": self.mobileno,
            "sex": self.sex,
            "address": self.address
        }

        registered_student.insert_one(registered_student_data)  # Insert the student data into the collection
        URI_CONNECTION.close()  # Close the MongoDB connection

