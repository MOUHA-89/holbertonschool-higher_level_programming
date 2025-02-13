#!/usr/bin/python3
"""
python program
"""
import pickle

class CustomObject:
    """
    this is a class
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"is_student: {self.is_student}")

    def serialize(self, filename):
        """
        method to print out the object’s attributes
        """
        with open(filename, "w", encosding= "UTF-8") as file:
            pickle.dump(self, file)
        
        with open(filename, "r", encosding="UTF-8") as file:

            return pickle.load(self)
        
    @classmethod 
    def deserialize(cls, filename):
        """
        This class method will take a filename as its parameter
        """

        with open(filename, "r", encoding="UTF-8") as file:
            
            return pickle.load(file)
