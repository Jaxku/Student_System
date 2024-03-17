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
    count = 0
    for student in student_list:
        if student.age >= age:
            student.display_info()
            count += 1
            student.display_info()
    return f"there are {count} students above {age}"


# Generate students from csv file
def generate_students():
    # available form classes are "BAKER" "MORGAN" "MCNICOL" "GRAHAM" "BELL"
    # "NIMMO" "BARKER"
    # available classes are "ART" "ENG" "MAT" "GRA" "DTC" "PHY" and "BIO"
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


def count_students():
    count = 0
    subject = input("Enter a subject: ").upper()
    for student in student_list:
        if subject in student.classes:
            count += 1
        if count > 0:
            return f"\n There are {count} students taking {subject}"
        else:
            return f"\n there are no students taking {subject}"


def find_student(text):
    name = input(text).title()
    for student in student_list:
        if student.name == name:
            student.display_info()
            return


# Main Routine
student_list = []   # Empty list to store students
generate_students()

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
print(select_age())






