#!/usr/bin/env python3
# This code defines a Person class with attributes name, age,
# and gender, and a method introduce that prints a greeting.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of the Person class
person_instance = Person(name="John Doe", age=30, gender="Male")

# Call the introduce method
person_instance.introduce()
