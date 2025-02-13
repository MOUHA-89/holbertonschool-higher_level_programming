#!/usr/bin/python3
"""
python program
"""
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file
    
    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
    """
    try:
        with open(filename, 'w', encoding= "UTF-8") as file:
            json.dump(data, file)
        print(f"Data successfully serialized and saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")


def load_and_deserialize(filename):
    """
    Save a python dictionary to JSON and serealise it to a file
    """
    try:
        with open(filename, 'r', encoding= "UTF-8") as file:
            data = json.load(file)
        print(f"Data successfully loaded and deserialized from {filename}.")
        return data
    except Exception as e:
        print(f"An error occurred while loading data from {filename}: {e}")
        return None