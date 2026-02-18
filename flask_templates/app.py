# Instead of returning hardcode HTML from the function, a HTML file can be rendered by the render_template() function.

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)
if __name__ == '__main__':
   app.run(debug = True)
