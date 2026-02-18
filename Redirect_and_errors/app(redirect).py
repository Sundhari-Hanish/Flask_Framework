from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('log_in.html')
@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['username'] == 'admin' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('index'))
@app.route('/success')
def success():
   return 'logged in successfully'
if __name__ == '__main__':
   app.run(debug = True)

# When you open the application, it shows a login page. If you enter admin, it redirects to the success page displaying “logged in successfully.” If you enter any other username, 
# it either redirects back to the login page or shows a 401 Unauthorized error (depending on the version used).
