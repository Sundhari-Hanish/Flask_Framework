# GET and POST Methods
# Program that takes data from an HTML form and Inserts it into SQLite database and displays the stored data.
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
def init_db():
    with sqlite3.connect("test1.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pname TEXT)""")
init_db()
@app.route("/")
def home():
    return render_template("form.html")
@app.route("/add", methods=["POST"])
def add_product():
    product_name = request.form["pname"]
    with sqlite3.connect("test1.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product(pname) VALUES(?)", (product_name,))
        conn.commit()
    return redirect(url_for("display"))
@app.route("/display")
def display():
    with sqlite3.connect("test1.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
    return render_template("display.html", products=products)
if __name__ == "__main__":
    app.run(debug=True)
