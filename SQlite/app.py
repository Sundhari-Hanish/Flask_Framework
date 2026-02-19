# Flask application demonstrating SQLite database integration with basic insert and display operations.
from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
# -----------------------------
# Create database and table
# -----------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    conn.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, city TEXT)")
    conn.close()
init_db()
# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("home.html")
# -----------------------------
# Add Student Page
# -----------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        city = request.form["city"]
        conn = sqlite3.connect("database.db")
        conn.execute("INSERT INTO students (name, city) VALUES (?, ?)", (name, city))
        conn.commit()
        conn.close()
        return "Student Added Successfully!"
    return render_template("add.html")
# -----------------------------
# View Students Page
# -----------------------------
@app.route("/list")
def list_students():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return render_template("list.html", rows=rows)
if __name__ == "__main__":
    app.run(debug=True)
