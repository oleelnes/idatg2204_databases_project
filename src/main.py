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
        modelname = request.args.get('modelname')
        if modelname:
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo \
            FROM `product` \
            WHERE model = '" + modelname + "'")
        else:        
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo FROM `product`")
        if skis > 0:
            skis = cur.fetchall()
        cur.close()
        return jsonify(skis), 200
    return "Sum ting went wong", 500

# Get orders from status as customer rep
@app.route('/customerrep', methods=['GET'])
def get_order_from_state():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        state = request.args.get('state')
        if state:
            order = cur.execute("SELECT * FROM `order` WHERE state = '" + state + "'")
        else: 
            cur.close()
            return "Bad request", 404
        if state > 0:
            order = cur.fetchall()
        cur.close()
        return jsonify(order), 200
    return "Error in db", 500

# Set order status as customer rep for spesific orderid
@app.route('/customerrep', methods=['POST'])
def get_order_from_state():
    legal = 0
    legalStates = []
    legalStates.append("being picked")
    legalStates.append("in transit")
    legalStates.append("waiting for pickup")
    legalStates.append("canceled")
    legalStates.append("completed")
    
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        orderid, state = request.args.get('orderid', 'state')
        if state and orderid:
            for val in legalStates:
                if state == val: 
                    legal = 1
            if legal == 1:
                order = cur.execute("SELECT * FROM `order` WHERE orderid = " + orderid)
                if order > 0:
                    order.fetchall()
                    change_order_state = cur.execute("UPDATE `order` SET `status`="+ state)
                    mysql.connection.commit()
                cur.close()
                order = cur.execute("SELECT * FROM `order` WHERE orderid = " + orderid)
                if order > 0:
                    order.fetchall() 
                return jsonify(order), 201
            else:
                cur.close()
                return "Bad request", 404   
    return "Error in db", 500
            



if __name__ == '__main__':
    app.run(debug=True)