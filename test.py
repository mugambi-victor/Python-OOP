#!/usr/bin/python3

class Robot:

    def __init__(self, name, build_year, city):
        self.__name = name
        self.__build_year = build_year
        self.__city = city

    def __getattr__(self, name):
        return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        self.__dict__[f"__{name}"] = value


robot = Robot("RoboBot", 2022, "TechCity")

print(robot.name)
print(robot.build_year)
print(robot.city)
