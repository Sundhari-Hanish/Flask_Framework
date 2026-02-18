from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'random string'
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index'))
   return render_template('login.html', error = error)
if __name__ == "__main__":
   app.run(debug = True)

#It checks whether the username or password entered in the login form is incorrect. The values come from `request.form`, which stores the data submitted through the HTML form using the POST method.
#If either the username or password is not `"admin"`, the login attempt fails.
#If both the username and password are correct (i.e., both are `"admin"`), the condition becomes **False**, so the `else` block runs. In that block, `flash()` stores a success message, 
#and `redirect(url_for('index'))` sends the user to the home page. This means the login is successful and the user is redirected with a success notification.
