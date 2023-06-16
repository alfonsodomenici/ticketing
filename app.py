from flask import Flask
from db_config import mysql
from flask import jsonify
from users_resource import users_res

app = Flask(__name__)

#db configuration
app.config['MYSQL_DATABASE_USER'] = 'ticketing'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ticketing'
app.config['MYSQL_DATABASE_DB'] = 'dbticketing'
app.config['MYSQL_DATABASE_HOST'] = '172.21.160.1'

mysql.init_app(app)

app.register_blueprint(users_res)

@app.route("/")
def hello():
    return "<p>Flask runnig</p>"


