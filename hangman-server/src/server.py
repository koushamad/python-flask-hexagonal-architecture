from flask import Flask
from src.infrastructure.flask_api import api
from dotenv import load_dotenv
from src.container import Container
from injector import Injector
from flask_injector import FlaskInjector
import os

# Load the .env file
load_dotenv()

app = Flask(__name__)
app.register_blueprint(api)

# Configure the Injector
injector = Injector([Container()])
FlaskInjector(app=app, injector=injector)

if __name__ == "__main__":
    debug = bool(os.getenv("FLASK_DEBUG", default=0))
    port = int(os.getenv("FLASK_RUN_PORT", default=5000))
    app.run(debug=debug, port=port)
