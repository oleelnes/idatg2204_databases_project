import json
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from hashlib import pbkdf2_hmac
import random
import endpoints.company.customer_rep as customer_rep
import endpoints.company.storekeeper as storekeeper
import endpoints.company.production_planner as prod_plan
import endpoints.public.public as public
import endpoints.customer.customer as customer
import endpoints.transport.transporter as transport

app = Flask(__name__)

app.config['MYSQL_HOST']="127.0.0.1"#"localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="idatg2204_2022_group12"

mysql = MySQL(app)

ALPHABET_AND_NUMBERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
role_user = "customer"

@app.route('/')
def index():
    message = "Up and running!\nSee the endpoints:\n\n/public"
    return message

# Public, gets information about all skis
@app.route('/public', methods=['GET'])
def get_skis():
    return public.get_skis(mysql)

# Retrieve orders in the "skis available" state
@app.route('/storekeeper/orders/skisavailable', methods=['GET'])
def get_skis_available_orders():
    if role_user != "storekeeper":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a storekeeper user at endpoint authentication/login"}'
        return json.loads(response), 401
    return storekeeper.get_skis_available_orders(mysql)

# Get orders from status as customer rep
@app.route('/customerrep/orders', methods=['GET'])
def get_order_from_state():
    if role_user != "customer rep":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer rep user at endpoint authentication/login"}'
        return json.loads(response), 401
    return customer_rep.get_order_from_state(mysql)

# Set order status as customer rep for spesific orderid
@app.route('/customerrep/order', methods=['PATCH'])
def change_order_state():
    if role_user != "customer rep":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer rep user at endpoint authentication/login"}'
        return json.loads(response), 401
    return customer_rep.change_order_state(mysql)

# Adds a new production plan from post with json
@app.route('/productionplanner', methods=['POST'])
def post_production_plan():
    if role_user != "productionplanner":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer rep user at endpoint authentication/login"}'
        return json.loads(response), 401
    return prod_plan.post_production_plan(mysql)

# Retrieve four week production plan summary

# Delete a given order
@app.route('/customer/cancelorder', methods=['DELETE'])
def delete_order():
    if role_user != "customer" and role_user != "customer rep" and role_user != "storekeeper":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer user at endpoint authentication/login"}'
        return json.loads(response), 401
    return customer.delete_order(mysql)


# Create new orders
@app.route('/customer/orders/new', methods=['POST'])
def place_order():
    if role_user != "customer" and role_user != "customer rep" and role_user != "storekeeper":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer user at endpoint authentication/login"}'
        return json.loads(response), 401
    return customer.place_order(mysql)

# Retrieve a four week production plan summary
@app.route('/customer/productionplan', methods=['GET'])
def get_production_plan_summary():
    if role_user != "customer" and role_user != "customer rep" and role_user != "storekeeper":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer user at endpoint authentication/login"}'
        return json.loads(response), 401
    return customer.get_production_plan_summary(mysql)

# Retrieve a specific order
@app.route('/customer/orderbyid', methods=['GET'])
def get_order_by_id():
    if role_user != "customer" and role_user != "customer rep" and role_user != "storekeeper":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer user at endpoint authentication/login"}'
        return json.loads(response), 401
    return customer.get_order_by_id(mysql)

# Retrieve orders with since filter
@app.route('/customer/orderssince', methods=['GET'])
def get_orders_since():
    if role_user != "customer" and role_user != "customer rep" and role_user != "storekeeper":
        response = '{"Error": "You are not authenticated for this endpoint.", \
            "Try": "Log into a customer user at endpoint authentication/login"}'
        return json.loads(response), 401
    return customer.get_orders_since(mysql)

# Create a new user and insert it into the database
@app.route('/authentication/newuser', methods=['POST'])
def new_user():
    if request.method ==  'POST':
        print("role: " + role_user)

        # User must be admin in order to create new users. TODO: change?
        if role_user != "admin":
            return "You are not authenticated for creating new users.", 401
        cur = mysql.connection.cursor()
        password = request.args.get('password')
        username = request.args.get('username') 
        role = request.args.get('role')

        if password is None or username is None or role is None:
            return "Wrong format. Please input username, password and role.", 400

        if username == "":
            return "Username cannot be empty.", 400

        # It is not allowed to create a user with the role admin
        if role == "admin":
            return "You don't have the authentication to create an admin user!", 401

        # Checking whether the role passed is valid or not
        if role != "customer" and role != "storekeeper" and role != "productionplanner" and \
            role != "transporter" and role != "customer rep":
            return "Please select a valid role (customer, customer rep, storekeeper, productionplanner, transporter).", 400

        # Checking if the username is already exists in the database.
        checkUsername = cur.execute("SELECT * FROM `authentication` WHERE username=%s", (username,))
        if checkUsername > 0:
            return "A user with that username already exists.", 403

        # Creating the salt and hashed password and inserting it into the database
        salt = createSalt()
        hashedpassword = createHashedPassword(password, salt)
        store = cur.execute("INSERT INTO `authentication` (`role`, `username`, `password_hashed`, `salt`) \
            VALUES (%s, %s, %s, %s)", (role, username, hashedpassword.hex(), salt,))
        mysql.connection.commit()

        stored = cur.execute("SELECT * FROM `authentication` WHERE username=%s", (username,))
        stored = cur.fetchall()
        cur.close()
        return jsonify(stored), 200
    return "Wrong method, only POST is supported.", 400

# Transporter get info about one or multiple orders in the ready to be shipped state
@app.route('/transport/orderinfo', methods=['GET'])
def get_order_info_ready_to_be_shipped():
    if role_user != "transporter":
        response = '{"Error": "You are not authenticated for this endpoint.", \
                "Try": "Log into a transporter user at endpoint authentication/login"}'
        return json.loads(response), 401
    return transport.get_order_info_ready_to_be_shipped(mysql)

# Changes the state of a shipment with order id in the Transporter endpoint
@app.route('/transport/orderstatus', methods=['PATCH'])
def change_shipment_state():
    if role_user != "transporter":
        response = '{"Error": "You are not authenticated for this endpoint.", \
                "Try": "Log into a transporter user at endpoint authentication/login"}'
        return json.loads(response), 401
    return transport.change_shipment_state(mysql)


# Login endpoint
@app.route('/authentication/login', methods=['POST'])
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
            return "Username not found in database.", (400)

        # Fetching data from the database.
        role_db = authentication_data[0]
        password_db = authentication_data[2]
        salt_db = authentication_data[3]

        if createHashedPassword(password, salt_db).hex() == password_db:
            # Sets the role_user variable which decides the level of authorization the user has.
            global role_user 
            role_user = role_db
            print("role: " + role_user)
            return "Successfully logged into user " + username + ", role: " + role_user, (200)
        else: 
            return "Wrong password.", (403)
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