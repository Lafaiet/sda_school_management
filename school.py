class Person:

    def __init__(self, name, age, nationality, gender):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender


class Student(Person):

    def __init__(self, name, age, group_name, email, *extra_args):
        self.group_name = group_name
        self.email = email
        super().__init__(name, age, *extra_args)


class Teacher(Person):

    def __init__(self, name, age, degree, capabilities):
        self.degree = degree
        self.capabilities = capabilities


class Subject:
    pass

student_1 = Student('Ivar', 20, 'EE9', 'ivar@gmail.com','Russian', 'N')

print(student_1.name)
print(student_1.age)
print(student_1.group_name)
print(student_1.email)
print(student_1.nationality)

student_2 = Student('Ivar', 20, 'EE9', 'ivar@gmail.com','Russian', 'N')

print(student_1==student_2)
