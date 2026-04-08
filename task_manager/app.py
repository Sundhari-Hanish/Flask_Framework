from flask import Flask
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from routes.task_routes import task_bp
def create_app():
    app = Flask(__name__)
    app.register_blueprint(task_bp)
    return app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
