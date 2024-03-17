""" Student System
"""


# Create a class called Student
class Student:
    def __init__(self, name, age, phone, form_class, classes, is_male):
        self.name = name
        self.age = age
        self.phone = phone
        self.form_class = form_class
        self.classes = classes
        # Gender stored as True False variable in IsMale
        self.is_male = is_male
        self.enrolled = True

        # Automatically append student to student list
        student_list.append(self)

    def display_info(self):
        print("####################")
        print(f"Name: {self.name}")
        print("####################")
        print(f"Age: {self.age}")
        print(f"Phone Number: {self.phone}")
        print(f"Form Class: {self.form_class}")
        print(f"Classes: {self.classes}")
        if self.is_male:
            print(f"{self.name} is female")
        print(f"Enrolled: {self.enrolled}")
        print()


# Function to invoke the display_info() function
def print_student_details():
    for student in student_list:
        student.display_info()


# Print students aged 16 or over - question 4a
def age_students():
    for student in student_list:
        if student.age >= 17:
            student.display_info()


# Print students over a specified age - question 4b
def select_age():
    age = int(input("Age to print above: "))
    for student in student_list:
        if student.age >= age:
            student.display_info()


# Main Routine
student_list = []   # Empty list to store students

# Instances of students
student1 = Student("Karen", 17, "123-4567", "WNLR", ["13DTC, 13SMX"], False)
student2 = Student("Bob", 18, "021-0263987", "BNNL", ["13SMX"], True)
student3 = Student("Lisa", 16, "022-1258755", "SKWR", ["13DTC, 13SMX"], False)
student4 = Student("Patrick", 18, "023-01234567", "SCBE", ["13DTC", "13ENG",
                                                           "13CMX"], True)

# Print student details
# print_student_details()
# age_students()
select_age()






