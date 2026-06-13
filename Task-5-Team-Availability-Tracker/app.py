from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('team.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS team(
        id INTEGER PRIMARY KEY,
        name TEXT,
        available INTEGER
    )
    ''')

    members = [
        (1, 'John', 1),
        (2, 'Emma', 0),
        (3, 'Michael', 1),
        (4, 'Sophia', 0)
    ]

    for member in members:
        cur.execute(
            "INSERT OR IGNORE INTO team VALUES(?,?,?)",
            member
        )

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members')
def members():
    conn = sqlite3.connect('team.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM team")
    data = cur.fetchall()

    conn.close()

    return jsonify(data)

@app.route('/toggle/<int:id>')
def toggle(id):

    conn = sqlite3.connect('team.db')
    cur = conn.cursor()

    cur.execute(
        '''
        UPDATE team
        SET available =
        CASE
            WHEN available=1 THEN 0
            ELSE 1
        END
        WHERE id=?
        ''',
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)