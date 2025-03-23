import sqlite3
from flask import Flask, render_template, request, jsonify
import csv
import json

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

def get_data_from_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    data = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in data]

def get_data_from_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_data_from_csv():
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.route('/')
def product_display():
    source = request.args.get('source', 'json')
    
    try:
        if source == 'json':
            data = get_data_from_json()
        elif source == 'csv':
            data = get_data_from_csv()
        elif source == 'sql':
            data = get_data_from_sqlite()
        else:
            return "Wrong source", 400

        return render_template('product_display.html', products=data)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    create_database()
    app.run(debug=True)