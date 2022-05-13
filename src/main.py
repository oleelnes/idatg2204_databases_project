from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from hashlib import pbkdf2_hmac
import random
import company.customer_rep as customer_rep

app = Flask(__name__)

app.config['MYSQL_HOST']="127.0.0.1"#"localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="idatg2204_2022_group12"

mysql = MySQL(app)

ALPHABET_AND_NUMBERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
role_user = ""

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
            WHERE model = %s", (modelname,))
        else:        
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo FROM `product`")
        if skis > 0:
            skis = cur.fetchall()
        cur.close()
        return jsonify(skis), 200
    return "Error in db", 500

# Retrieve orders in the "skis available" state
@app.route('/storekeeper/orders/skisavailable', methods=['GET'])
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
            order = cur.execute("SELECT * FROM `order` WHERE order_status=%s", (state,))
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
    legalStates.append("ready to be shipped")
  
    
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
                order = cur.execute("SELECT * FROM `order` WHERE id = %s", (orderid,))
                if order > 0:
                    order = cur.fetchall()
                    change_order_state = cur.execute("UPDATE `order` SET `order_status`=%s", (state,))
                    mysql.connection.commit()
                    if state == "fulfilled":
                        create_transport_request(orderid)
                order = cur.execute("SELECT * FROM `order` WHERE id = %s", (orderid,))
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
    order = cur.execute("SELECT id FROM `order` WHERE id = %s AND order_status = 'fulfilled'", (orderid,))
    if order > 0:
        transport = cur.execute("INSERT INTO `shipment` (`order_id`) VALUES (%s)", (orderid,))#"SELECT * FROM `transport`
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
            plan = cur.execute("INSERT INTO `production_plan` (`week_number`, `manafacturer_id`) VALUES (%s, '200000')", (week,))
            mysql.connection.commit()
            typeData = cur.execute("INSERT INTO `production_type` \
                (`production_week_number`, `product_id`, `day`, `type`, `production_amount`) \
                VALUES (%s, %s, %s, %s, %s)", (week, productid, day, type, productionAmount,))
            mysql.connection.commit()
            week += 1

        prodplan = cur.execute("SELECT * FROM `production_type` WHERE production_week_number BETWEEN %s AND %s", (week - 3, week,))
        if prodplan > 0:
            prodplan = cur.fetchall()
            cur.close()
            return jsonify(prodplan), 201
    else:
        cur.close()
        return "Bad request", 404   
    return "Internal error in database", 500 #todo


# Retrieve four week production plan summary

# Delete a given order
@app.route('/customer/cancelorder', methods=['DELETE'])
def delete_order():
    if request.method == 'DELETE':
        cur = mysql.connection.cursor()
        cur.close()
    else:
        return "Wrong method. Only GET is supported.", 405


# Create new orders
@app.route('/customer/orders/new', methods=['POST'])
def place_order():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        orderData = request.get_json()

        id = orderData['id']
        productId = orderData['product_id']
        customerId = orderData['customer_id']
        skiType = orderData['ski_type']
        quantity = orderData['quantity']
        totalPrice = orderData['total_price']
        orderStatus = orderData['order_status']

        #todo: create id instead of having user decide it. 

        order = cur.execute("INSERT INTO `order` (`id`, `product_id`, `customer_id`, `ski_type`, `quantity`, `total_price`, `order_status`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, productId, customerId, skiType, quantity, totalPrice, orderStatus,))
        mysql.connection.commit()
        cur.close()
        return jsonify(order), 200
    else: 
        return "Wrong method. Only POST is supported.", 405

# get all orders
@app.route('/customer/orders', methods=['GET'])
def get_production_plan_summary():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.close()
    else:
        return "Wrong method. Only GET is supported.", 405



# Retrieve a specific order
@app.route('/customer/orderbyid', methods=['GET'])
def get_order_by_id():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        id = request.args.get('order_id')
        retrieved_order = cur.execute("SELECT * FROM `order` WHERE `id`=%s", (id,))
        cur.close()
        return jsonify(retrieved_order), 200
    else:
        return "Wrong method. Only GET is supported.", 405

# Retrieve orders with since filter
@app.route('/customer/orders', methods=['GET'])
def get_orders_since():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.close()
    else:
        return "Wrong method. Only GET is supported.", 405




# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        login_data = request.get_json()
        username = login_data['username']
        password = login_data['password']

        resp = cur.execute("SELECT * FROM `authentication` WHERE `username`=%s", (username,))

        # Checks if resp has any content and stores it as an array if it does. If not, an error is returned.
        if resp > 0:
            authentication_data = cur.fetchone()
            cur.close()
        else:
            cur.close()
            return "Username not found in database." (400)

        # Fetching data from the database.
        role_db = authentication_data[0]
        password_db = authentication_data[2]
        salt_db = authentication_data[3]

        if createHashedPassword(password, salt_db).hex() == password_db:
            # Sets the role_user variable which decides the level of authorization the user has.
            role_user = role_db
            return "Successfully logged into user " + username + ", role: " + role_user, (200)
        else: 
            return "Wrong password.", (400)
    else:
        cur.close()
        return "Method not supported. Try again with POST method.", (501)

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