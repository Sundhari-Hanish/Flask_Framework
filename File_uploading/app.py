from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
if __name__ == '__main__':
   app.run(debug = True)

#This Flask app creates a simple file upload system.
#When a user visits `/upload`, it shows an HTML form to choose a file.
#After submitting, the form sends the file to `/uploader` using a POST request.
#Flask receives the file, secures its name using `secure_filename()`, saves it to the server, and returns a success message.
