import hashlib
from config import Client


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

        password_bytes = self.password.encode('utf-8')  # Encode password as bytes
        # Print the password value before hashing
        print("Password Value:", self.password)
        # Hash the password using SHA256
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(password_bytes)
        hashed_password = hash_algorithm.hexdigest()

        registered_student_data = {
            "name": self.name,
            "password": hashed_password,
            "course": self.course,
            "schoolname": self.schoolname,
            "emailid": self.emailid,
            "mobileno": self.mobileno,
            "sex": self.sex,
            "address": self.address
        }

        try:
            registered_student.insert_one(registered_student_data)  # Insert the student data into the collection
            return True
        except:
            return False

    def get_student_data(self):
        db_student = Client["studentdata"]
        registered_student = db_student["registeredstudents"]

        try:
            filter = {
                'emailid': self.emailid,
            }

            # Execute the query
            result = registered_student.find_one(filter, {'_id': 0})
            return result
        except:
            return None
