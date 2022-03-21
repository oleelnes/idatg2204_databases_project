from crypt import methods
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="127.0.0.1"#"localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="idatg2204_2022_group12"

mysql = MySQL(app)

@app.route('/')
def index():
    message = "Up and running!\nSee the endpoints:\n\n/public"
    return message

@app.route('/public', methods=['GET'])
def get_skis():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        skis = cur.execute("SELECT * FROM `product`")
        if skis > 0:
            skis = cur.fetchall()
        cur.close()
        return jsonify(skis), 200
    return "Sum ting went wong", 500

if __name__ == '__main__':
    app.run(debug=True)