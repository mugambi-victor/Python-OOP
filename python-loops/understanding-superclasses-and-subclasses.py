#!/usr/bin/python3

class Schoolmember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("initialized School member: {}".format(self.name))


    def tell(self):
        """print my details"""
        print("Name-{}\nAge-{}".format(self.name, self.age))

class Teacher(Schoolmember):
    def __init__(self, name, age, salary):
        Schoolmember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher: {}".format(self.name))

    def tell(self):
        Schoolmember.tell(self)
        print("salary-{:d}".format(self.salary))
class Student(Schoolmember):
    def __init__(self, name, age, marks):
        Schoolmember.__init__(self, name, age)
        self.marks = marks
        print("initialized Student: {}".format(self.name))

    def tell(self):
        Schoolmember.tell(self)
        print("marks-{:d}".format(self.marks))



student = Student("Victor Mugambi", 24, 339)
teacher = Teacher("Mr Gichohi", 24, 339)
members = [teacher, student]
''' using a for loop to iterate over the list of objects'''
for member in members:
    member.tell()
