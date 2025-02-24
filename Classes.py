class Student:
    def __init__(self, fname, lname, admno, course, dept, email):
        self.fname = fname
        self.lname = lname
        self.admno = admno
        self.course = course
        self.dept = dept
        self.email = email

student_1 = Student("Riziki", "Antonie", 23357, "Dip in ICT", "ICT", "antonriziki@gmail.com")
student_2 = Student("Geoffrey", "Habil", 23789, "Dip in Health Records", "Health and Science", "habshikanda@gmail.com")

print("First Name : " + "\t" + student_1.fname)
print("Last Name : " + "\t" + student_1.lname)
print("E-mail :" + "\t" + student_1.email)
print("Admission No. :" + "\t" + str(student_1.admno))
print("Course :" + "\t" + student_1.course)
print("Department : " + "\t" + student_1.dept)


