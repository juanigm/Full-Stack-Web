from email.headerregistry import AddressHeader
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """The root"""
    return 'Hello World'

app.debug = True
app.run()