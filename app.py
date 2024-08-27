from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a securely generated key

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        active BOOLEAN NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/create', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    active = True if 'active' in request.form else False
    
    if username and password:
        hashed_password = generate_password_hash(password)  # Hash the password
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO User (username, password, active)
            VALUES (?, ?, ?)
            ''', (username, hashed_password, active))
            conn.commit()
            conn.close()
            flash("User created successfully!")
        except sqlite3.IntegrityError:
            flash("Username already exists!", "error")
    else:
        flash("Please provide both username and password!", "error")
    
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_user():
    user_id = request.form['id']
    username = request.form['username']
    password = request.form['password']
    active = True if 'active' in request.form else False
    
    hashed_password = generate_password_hash(password)  # Hash the password
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE User SET username = ?, password = ?, active = ? WHERE id = ?
    ''', (username, hashed_password, active, user_id))
    conn.commit()
    conn.close()
    
    flash("User updated successfully!")
    return redirect(url_for('index'))

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM User WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    
    flash("User deleted successfully!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
