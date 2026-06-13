from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.json
    note = data['note']

    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO notes (content) VALUES (?)",
        (note,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Note saved successfully"})

@app.route('/get_notes')
def get_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()

    conn.close()

    return jsonify(notes)

if __name__ == '__main__':
    app.run(debug=True)