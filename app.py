from flask import Flask

from sync import get_local_data

data = get_local_data()  # Load data eagerly
app = Flask(__name__)


@app.route("/")
def get_data():
    return data, 200
