#!/usr/bin/python3
"""
python program
"""
import json

def serialize_and_save_to_file(data, filename):
    """
    serialize a Python dictionary to a JSON file
    """
    with open(filename, 'w', encoding= "UTF-8") as file:
            json.dump(data, file)


def load_and_deserialize(filename):
    """
    deserialize the JSON file to recreate the Python Dictionary.
    """
    with open(filename, 'r', encoding= "UTF-8") as file:
             return json.load(file)
