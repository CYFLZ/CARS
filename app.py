from flask import Flask
from config import Config
from Routes import load_routes
from flask_mysqldb import MySQL
import os



app = Flask(__name__)


app.config.from_object(Config)
mysql = MySQL(app)
app.mysql = mysql
 


load_routes(app) 
X = "Hola "
 
# app.run(debug=True, port=5000, host='0.0.0.0')
