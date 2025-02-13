#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to save the serialized data.

    Returns:
        None
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data successfully serialized and saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")

def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file to recreate a Python dictionary.

    Parameters:
        filename (str): The name of the file to load and deserialize.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data successfully loaded and deserialized from {filename}.")
        return data
    except Exception as e:
        print(f"An error occurred while loading data from {filename}: {e}")
        return None
