from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Homepage route to display data
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

# Route to add data
@app.route('/add', methods=['POST'])
def add_data():
    name = request.form['name']
    age = request.form['age']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()  # Initialize database only once
    app.run(debug=True)
