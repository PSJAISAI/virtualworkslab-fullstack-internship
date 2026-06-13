from flask import Flask, render_template, jsonify
import sqlite3
import requests

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect('quotes.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS quotes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT,
        author TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Get Random Quote
@app.route('/quote')
def get_quote():

    response = requests.get(
        'https://dummyjson.com/quotes/random'
    )

    data = response.json()

    quote = data['quote']
    author = data['author']

    # Save to Database
    conn = sqlite3.connect('quotes.db')
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO quotes (quote, author) VALUES (?, ?)",
        (quote, author)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "quote": quote,
        "author": author
    })

# Quote History
@app.route('/history')
def history():

    conn = sqlite3.connect('quotes.db')
    cur = conn.cursor()

    cur.execute(
        "SELECT quote, author FROM quotes ORDER BY id DESC"
    )

    data = cur.fetchall()

    conn.close()

    return jsonify(data)

# Run App
if __name__ == '__main__':
    app.run(debug=True)