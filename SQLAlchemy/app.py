from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
# Create Flask app
app = Flask(__name__)
# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "mysecretkey"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # removes warning
# Create SQLAlchemy object
db = SQLAlchemy(app)
# Create Model (Table)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
# Home Page - Shows All Students
@app.route('/')
def show_all():
    students = Student.query.all()
    return render_template('show_all.html', students=students)
# Add New Student
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields')
        else:
            student = Student(
                request.form['name'],
                request.form['city'],
                request.form['addr'],
                request.form['pin']
            )
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')
# Run App (FIXED SECTION)
if __name__ == '__main__':
    with app.app_context():  
        db.create_all()       
    app.run(debug=True)
