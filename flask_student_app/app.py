# Flask project with template rendering and flash messages
from flask import Flask, render_template,request,redirect,url_for,flash
app=Flask(__name__)
app.secret_key="supersecretkey"
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name = request.form.get("name")
        email=request.form.get("email")
        if not name or not email:
            flash("All fields are required","error")
            return redirect(url_for("register"))
        flash(f"Student {name} registered successfully!","success")
        return redirect(url_for("home"))
    return render_template("register.html")
if __name__=="__main__":
    app.run(debug=True)
