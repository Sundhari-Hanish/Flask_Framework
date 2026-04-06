from flask import Flask
from routes.product_routes import product_bp
app = Flask(__name__)
app.register_blueprint(product_bp)
if __name__ == "__main__":
    app.run(debug=True) 
