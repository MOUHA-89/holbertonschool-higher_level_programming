#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file.py
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file.py

data = ["apple", "banana", "cherry"]

with open("add_item.json", "w") as file:
    json.dump(data, file)
