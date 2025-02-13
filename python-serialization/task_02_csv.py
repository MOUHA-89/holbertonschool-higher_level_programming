#!/usr/bin/python3
"""
python program
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    function that takes the CSV filename as its parameter
    and writes the JSON data to data.json.
    """
    try:

        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        json_data = json.dumps(data, indent=2)

        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
