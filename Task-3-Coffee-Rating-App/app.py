from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS coffee(
        id INTEGER PRIMARY KEY,
        name TEXT,
        votes INTEGER
    )
    ''')

    coffees = [
        (1,'Espresso',0),
        (2,'Cappuccino',0),
        (3,'Latte',0),
        (4,'Mocha',0)
    ]

    for coffee in coffees:
        cur.execute(
            "INSERT OR IGNORE INTO coffee VALUES(?,?,?)",
            coffee
        )

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/coffees')
def coffees():
    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM coffee")
    data = cur.fetchall()

    conn.close()

    return jsonify(data)

@app.route('/vote/<int:id>')
def vote(id):

    conn = sqlite3.connect('coffee.db')
    cur = conn.cursor()

    cur.execute(
        "UPDATE coffee SET votes=votes+1 WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"success":True})

if __name__ == '__main__':
    app.run(debug=True)