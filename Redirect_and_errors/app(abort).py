from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('log_in.html')
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      if request.form['username'] == 'admin' :
         return redirect(url_for('success'))
      else:
         abort(401)
   else:
      return redirect(url_for('index'))
@app.route('/success')
def success():
   return 'logged in successfully'
if __name__ == '__main__':
   app.run(debug = True)

#This Flask application shows a login page at /. When the form is submitted to /login, it checks if the username is admin—if yes, it redirects to /success and displays “logged in successfully.”
#If the username is incorrect, it stops the program using abort(401) and shows a 401 Unauthorized error page.
