from flask import Flask
from pages import index

# app file for 
app = Flask(__name__)

# add routes to python file
app.add_url_rule('/','index', index.index)