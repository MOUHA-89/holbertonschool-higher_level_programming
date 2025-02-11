#!/usr/bin/python3
class Student:
    """
    A class that defines a student by their first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
    
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

# Example usage to get the desired output
student_1 = Student("John", "Doe", 23)
print(student_1.to_json())

student_2 = Student("Bob", "Dylan", 27)
print(student_2.to_json(['first_name', 'age']))

print(student_2.to_json(['age']))
