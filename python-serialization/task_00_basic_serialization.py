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
    print(f"Data successfully serialized and saved to {filename}.")


def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file
    """
    with open(filename, 'r', encoding= "UTF-8") as file:
            data = json.load(file)
    print(f"Data successfully loaded and deserialized from {filename}.")
    
    
