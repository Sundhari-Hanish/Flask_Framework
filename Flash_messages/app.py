# Flask application demonstrating flash messages with basic form validation
from flask import Flask, render_template,request,redirect,url_for, flash
app=Flask(__name__)
app.secret_key="supersecretkey"
@app.route("/") 
def home():
    return render_template("index.html")
@app.route("/submit",methods=["POST"])
def submit():
    username = request.form.get("username")
    if not username:
        flash("Username cannot be empty!","error")
        return redirect(url_for("home"))
    flash(f"Welcome,{username}!You have logged in successfully.", "success")
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run(debug=True)
