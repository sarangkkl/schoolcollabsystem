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

        try:
            students= list(registered_student.find({}))
            print("STUDENT")
            print(students)



            if students:
                for student in students:
                    if registered_student_data['name'] == student['name']:
                        found= 1
                    else:
                        found = 0

                if not found:
                    registered_student.insert_one(registered_student_data)  # Insert the student data into the collection
                    print("Inserted new")
                    return True
                else:
                    return False
            else:
                registered_student.insert_one(registered_student_data)  # Insert the student data into the collection
                print("Inserted new")
                return True

        except:
            print('Error')
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
