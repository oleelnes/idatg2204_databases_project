from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="127.0.0.1"#"localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="banking"

mysql = MySQL(app)

@app.route('/')
def index():
    return "Up and running!"

if __name__ == '__main__':
    app.run(debug=True)