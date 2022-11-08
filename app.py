# import the Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
# "/" denotes that we want to put our data at the root of our routes
@app.route('/')
def hello_world():
    return 'Hello world'

# This command sets the FLASK_APP environment variable to the name of our Flask file, app.py.

