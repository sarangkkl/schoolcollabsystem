from model.newstudent import Student

def add_student(name, course ,schoolname ,emailid , mobileno, sex, address):
    student = Student(name, course ,schoolname ,emailid , mobileno, sex, address)
    #Code to check validity of student
    #-----End of validation

    student.save()
