#!/usr/bin/python3
import sys
from os import path

# Importing the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# File name where the list will be saved
filename = "add_item.json"

# Load existing data if the file exists, otherwise start with an empty list
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
