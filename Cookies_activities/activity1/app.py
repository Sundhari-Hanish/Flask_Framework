from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/")
def home():
    name = request.cookies.get("username")   #read cookie
    if name:
        return f"Welcome back {name}"
    return "Hello! Please login"
@app.route("/set/<name>")
def set_cookie(name):
    response = make_response(f"Cookie set for {name}")
    response.set_cookie("username", name)   #set cookie
    return response
@app.route("/delete")
def delete_cookie():
    response = make_response("Cookie deleted")
    response.delete_cookie("username")   #delete cookie
    return response
if __name__ == "__main__":
    app.run(debug=True)
