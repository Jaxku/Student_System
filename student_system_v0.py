"""
Student Class System, V1
"""


# Create a class called Students
class Students:
    def __init__(self, name, age, phone_number, form_class,
                 subjects, is_male, enrolled_in_class):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male
        self.enrolled_in_class = enrolled_in_class


# Main Routine
student_list = []

# Create students objects
# s1 = Students("Karen, 17, 123-4567, WNLR, 13DTC, True, false") PREVIOUS LINE
s1 = Students(name="Karen", age=17, phone_number="123-4567",
              form_class="WNLR", subjects="13DTC",
              is_male=False, enrolled_in_class=True)
s2 = Students(name="Bob", age=18, phone_number="021-0263674",
              form_class="BNNL", subjects="13SMX",
              is_male=True, enrolled_in_class=True)


print(s1)




