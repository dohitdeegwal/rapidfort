from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
