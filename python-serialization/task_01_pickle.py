#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"is_student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "w", encoding="UTF-8") as file:
                pickle.dump(self, file)

        except Exception as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "r", encoding="UTF-8") as file:
                pickle.load(file)

        except Exception as e:
            print(f"Error deserializing object:{e}")
            return None
