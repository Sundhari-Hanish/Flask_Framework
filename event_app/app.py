from flask import Flask, render_template, redirect, url_for
from forms import EventForm
import sqlite3
app = Flask(__name__)
app.secret_key = "supersecretkey" 
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    form = EventForm()
    if form.validate_on_submit():
        name = form.full_name.data
        email = form.email.data
        domain = form.tech_domain.data
        with sqlite3.connect("event.db") as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO participants (name, email, domain) VALUES (?, ?, ?)""", (name, email, domain))
            con.commit()
        return render_template("success.html", name=name)
    return render_template("register.html", form=form)
@app.route("/view")
def view():
    con = sqlite3.connect("event.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM participants")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)
if __name__ == "__main__":
    app.run(debug=True)
    
