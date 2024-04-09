#!/usr/bin/python3
# getter methods- retrieve values of attributes
# setter methds - can change the values of attributes
# Each attribute must have these two methds if they are to be accessed.


class SchoolMember:
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age
    def sayHi(self):
        print("hello {}".format(self.__name))

    def setName(self, name):
        self.__name = name
    def getName(self, name):
        return self.__name
student = SchoolMember("Victor", 23)
student1 = SchoolMember()
student1.setName("Victor Mugambi")
student1.sayHi()
