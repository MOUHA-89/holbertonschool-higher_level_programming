from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_json_data():
    with open('products.json', 'r') as file:
        return json.load(file)

def get_csv_data():
    data = []
    with open('products.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def get_sql_data():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    data = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return data

@app.route('/')
def display_products():
    source = request.args.get('source', 'json')
    
    try:
        if source == 'json':
            data = get_json_data()
        elif source == 'csv':
            data = get_csv_data()
        elif source == 'sql':
            data = get_sql_data()
        else:
            return render_template('product_display.html', error="Wrong source")
        
        return render_template('product_display.html', products=data)
    except (FileNotFoundError, json.JSONDecodeError, csv.Error, sqlite3.Error) as e:
        return render_template('product_display.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)