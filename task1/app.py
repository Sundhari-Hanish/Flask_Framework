# Flask app to manage customer complaints using SQLite database storage
from flask import Flask,render_template,request,redirect,url_for
import time
import sqlite3
app=Flask(__name__)
def init_db():
    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            customer_id TEXT,
            complaint_type TEXT,
            complaint TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()
@app.route("/")
def welcome():
    return render_template("welcome.html")
@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        customer_name=request.form["name"]
        customer_id=request.form["id"]
        complaint_type=request.form["type"]
        complaint=request.form["complaint"]
        c_time=time.ctime()
        customer_details={
            "Cust_name":customer_name,
            "Cust_id":customer_id,
            "Complaint_type":complaint_type,
            "Complaint": complaint,
            "Time":c_time
        }
        conn = sqlite3.connect("complaints.db")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO complaints (customer_name, customer_id, complaint_type, complaint, time) VALUES (?, ?, ?, ?, ?)""", (customer_name, customer_id, complaint_type, complaint, c_time))
        conn.commit()
        conn.close()
        return render_template("display.html",data=customer_details)
    return render_template("add.html")
@app.route("/data")
def data():
    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()
    cursor.execute("SELECT customer_name, customer_id, complaint_type, complaint, time FROM complaints")
    complaints = cursor.fetchall()
    conn.close()
    return render_template("data.html", complaints=complaints)
if __name__=="__main__":
    init_db()
    app.run(debug=True)
