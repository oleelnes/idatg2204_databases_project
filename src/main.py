from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from hashlib import pbkdf2_hmac
import random

app = Flask(__name__)

app.config['MYSQL_HOST']="127.0.0.1"#"localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="idatg2204_2022_group12"

mysql = MySQL(app)

ALPHABET_AND_NUMBERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

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

# Retrieve orders in the "skis available" state
@app.route('/storekeeper/orders', methods=['GET'])
def get_skis_available_orders():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        order = cur.execute("SELECT * FROM `order` WHERE order_status = 'skis available'")
        if order:
            order = cur.fetchall()
            cur.close()
            return jsonify(order), 200
        else:
            cur.close()
            return "Bad request", 400
        #something
    return "Error in db", 500

# Get orders from status as customer rep
@app.route('/customerrep/orders', methods=['GET'])
def get_order_from_state():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        state = request.args.get('state')
        if state:
            order = cur.execute("SELECT * FROM `order` WHERE order_status = '" + state + "'")
        else: 
            cur.close()
            return "Bad request", 404
        if state != "":
            order = cur.fetchall()
        cur.close()
        return jsonify(order), 200
    return "Error in db", 500



# Set order status as customer rep for spesific orderid
@app.route('/customerrep/order', methods=['PATCH'])
def post_order_state():
    legal = 0
    legalStates = []
    legalStates.append("new")
    legalStates.append("open")
    legalStates.append("skis available")
    legalStates.append("closed")
    legalStates.append("being picked")
    legalStates.append("in transit")
    legalStates.append("waiting for pickup")
    legalStates.append("canceled")
    legalStates.append("completed")
    legalStates.append("fulfilled")
    
    if request.method == 'PATCH': 
        cur = mysql.connection.cursor()
        content = request.get_json(silent=True)
        orderid = None
        state = None
        if content:
            orderid = content['orderid']
            state = content['state']

        if orderid is None or state is None:
            orderid, state = request.args.get('orderid', 'state')
        
        if state and orderid:
            for val in legalStates:
                if state == val: 
                    legal = 1
            if legal == 1:
                order = cur.execute("SELECT * FROM `order` WHERE id = " + orderid)
                if order > 0:
                    order = cur.fetchall()
                    change_order_state = cur.execute(f"UPDATE `order` SET `order_status`='{state}'")
                    mysql.connection.commit()
                    if state == "fulfilled":
                        create_transport_request(orderid)
                order = cur.execute("SELECT * FROM `order` WHERE id = " + orderid)
                if order > 0:
                    order = cur.fetchall() 
                return jsonify(order), 201
            else:
                cur.close()
                return "Bad request", 404   
        return "Bad request", 404
    return "Error in db", 500

# Creates a new transport request from the given orderID input parameter            
def create_transport_request(orderid):
    cur = mysql.connection.cursor()
    order = cur.execute(f"SELECT id FROM `order` WHERE id = {orderid} AND order_status = 'fulfilled'")
    if order > 0:
        transport = cur.execute(f"INSERT INTO `shipment` (`order_id`) VALUES ({orderid})")#"SELECT * FROM `transport`
        mysql.connection.commit()
    cur.close()


# Adds a new production plan from post with json
@app.route('/productionplanner', methods=['POST'])
def post_production_plan():
    cur = mysql.connection.cursor()
    content = request.get_json()
    month = content['month']
    productid = content['productid']
    day = content['day']
    type = content['type']
    productionAmount = content['productionAmount']

    if month != "" and productid != "":
        week = 4 * int(month)
        weeks = range(4)
        for i in weeks:
            plan = cur.execute(f"INSERT INTO `production_plan` (`week_number`, `manafacturer_id`) VALUES ('{week}', '200000')")
            mysql.connection.commit()
            typeData = cur.execute(f"INSERT INTO `production_type` \
                (`production_week_number`, `product_id`, `day`, `type`, `production_amount`) \
                VALUES ('{week}', '{productid}', '{day}', '{type}', '{productionAmount}')")
            mysql.connection.commit()
            week += 1

        prodplan = cur.execute(f"SELECT * FROM `production_type` WHERE production_week_number BETWEEN {week - 3} AND {week}")
        if prodplan > 0:
            prodplan = cur.fetchall()
            cur.close()
            return jsonify(prodplan), 201
    else:
        cur.close()
        return "Bad request", 404   
    return "Error in db", 500 #todo

# Function that returns a randomly generated salt for authentication purposes.
def createSalt():
    salt=[]
    for i in range(12):
        salt.append(random.choice(ALPHABET_AND_NUMBERS))
    return "".join(salt)

# Function that returns a hashed password with sha256 and salt.
def createHashedPassword(password, salt):
    return pbkdf2_hmac('sha256', str.encode(password), str.encode(salt), 200000)



if __name__ == '__main__':
    app.run(debug=True)