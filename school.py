from abc import ABC, abstractmethod
from dataclasses import dataclass
from copy import copy, deepcopy


@dataclass
class Body:
    height: int
    weight: float

    def bmi(self):
        return self.height * self.weight


class Person:

    def __init__(self, name, age, nationality, gender):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender

    def display(self):
        print('------------------------')
        print(self.name)
        print(self.age)
        print(self.nationality)
        print(self.gender)

    def login(self):
        print('You are logged in from the Person class ')


class Player(ABC):

    def play(self):
        print('I am having fun...')
        self.espefic_play()

    @abstractmethod
    def espefic_play(self):
        pass


class Student(Person, Player):

    def __init__(self, name, age, group_name, email, fav_animal, *extra_args):
        self.group_name = group_name
        self.email = email
        self.grades = None
        self.fav_animal = fav_animal
        Person.__init__(self, name, age, *extra_args)

    def display(self):
        Person.display(self)
        print(self.group_name)
        print(self.email)

    def grades_avg(self):
        if self.grades is None:
            return None
        else:
            avg = sum(self.grades)/len(self.grades)
            return avg

    def espefic_play(self):
        print('I am playing with video game')


class Staff:

    def calculate_salary(self):
        self.salary = self.base_salary + self.base_salary * .1

    def __init__(self, base_salary):
        self.base_salary = base_salary
        self.calculate_salary()

    def register_taxes(self):
        print('<from Staff class> Registering taxes...')


class TeachingSubject:

    def __init__(self, name):
        self.name = name


class Teacher(Person, Staff, Player):

    def __init__(self, name, age, degree, capabilities, base_salary, *extra_args):
        self.degree = degree
        self.capabilities = capabilities
        Staff.__init__(self, base_salary)
        Person.__init__(self, name, age, *extra_args)

    def display(self):
        Person.display(self)
        print(self.degree)
        print(self.capabilities)

    def espefic_play(self):
        print('I am playing with ball')



class Coordinator(Person, Staff):

    def __init__(self, name, age, groups, base_salary, *extra_args):
        self.groups = groups
        Staff.__init__(self, base_salary)
        Person.__init__(self, name, age, *extra_args)

    def display(self):
        Person.display(self)
        print(self.groups)



class Subject:
    pass


student_1 = Student('Ivar', 20, 'EE9', 'ivar@gmail.com', 'dog','Russian', 'N')
student_2 = Student('Andre', 25, 'EE10', 'andre@gmail.com','cat', 'Russian', 'N')


student_1.grades = [10, 5, 5, 7, 8, 9, 10]
avg = student_1.grades_avg()

student_2.grades = [5, 5, 5, 7, 8, 9, 3]
avg = student_2.grades_avg()

python_subject = TeachingSubject('Python')

teacher1 = Teacher('Lafaiet', 30, 'master', [python_subject], 100, 'Brazilian', 'M')

coord1 = Coordinator('Salome', 25, ['python9'], 800, 'Polish', 'F')

my_body = Body(178, 87)

your_body = Body(178, 87)

student_1.favorite_teacher = teacher1

student_1_copy = deepcopy(student_1)
student_1_copy.name = 'Putin'
student_1_copy.favorite_teacher.name = 'Mike'
student_1_copy.display()
print(student_1.favorite_teacher.name)

student_1.display()
print(student_1_copy.favorite_teacher.name)