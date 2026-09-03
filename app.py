from flask import Flask
from config import Config
from Routes import load_routes
from flask_mysqldb import MySQL




app = Flask(__name__)


app.config.from_object(Config)
mysql = MySQL(app)
app.mysql = mysql
load_routes(app) 

print("MYSQL_HOST:", app.config.get("MYSQL_HOST"))
print("MYSQL_PORT:", app.config.get("MYSQL_PORT"))
print("MYSQL_USER:", app.config.get("MYSQL_USER"))
print("MYSQL_DB:", app.config.get("MYSQL_DB"))
print("MYSQL_SSL:", app.config.get("MYSQL_SSL"))
print("CA existe:", os.path.exists("/etc/secrets/aiven-ca.pem"))
 
# app.run(debug=True, port=5000, host='0.0.0.0')
