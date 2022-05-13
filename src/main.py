from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from hashlib import pbkdf2_hmac
import random
import company.customer_rep as customer_rep
import company.storekeeper as storekeeper
import public.public as public

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
    return public.get_skis(mysql)

# Retrieve orders in the "skis available" state
@app.route('/storekeeper/orders/skisavailable', methods=['GET'])
def get_skis_available_orders():
    return storekeeper.get_skis_available_orders(mysql)

# Get orders from status as customer rep
@app.route('/customerrep/orders', methods=['GET'])
def get_order_from_state():
    return customer_rep.get_order_from_state(mysql)

# Set order status as customer rep for spesific orderid
@app.route('/customerrep/order', methods=['PATCH'])
def post_order_state():
    return customer_rep.post_order_state(mysql)

# Adds a new production plan from post with json
@app.route('/productionplanner', methods=['POST'])
def post_production_plan():
    return storekeeper.post_production_plan(mysql)

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
        date = orderData['date']

        if id is None or productId is None or customerId or skiType \
        is None or quantity is None or totalPrice is None or orderStatus is None or date is None:
            return "Something is wrong in the json body!", 400

        #todo: create id automatically instead of having user decide it. 

        order = cur.execute("INSERT INTO `order` (`id`, `product_id`, `customer_id`, `ski_type`, `quantity`, `total_price`, `order_status`, `date`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, productId, customerId, skiType, quantity, totalPrice, orderStatus, date))
        mysql.connection.commit()

        order_response = cur.execute("SELECT * FROM `order` WHERE id=%s", (id,))
        order_response = cur.fetchall()

        cur.close()
        return jsonify(order_response), 200
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
        retrieved_order = cur.fetchall()
        cur.close()
        return jsonify(retrieved_order), 200
    else:
        return "Wrong method. Only GET is supported.", 405

# Retrieve orders with since filter
@app.route('/customer/orderssince', methods=['GET'])
def get_orders_since():
    if request.method == 'GET':
        cur = mysql.connection.cursor()

        date = request.args.get('date')

        if date is None:
            return "Date must be entered as a key.", 400
        
        #"SELECT * FROM `order` BETWEEN %s AND CURDATE() ORDER BY date asc"
        orders = cur.execute("SELECT * FROM `order` WHERE `date` BETWEEN %s AND CURDATE() ORDER BY date asc", (date,))
        orders = cur.fetchall()
        cur.close()

        return jsonify(orders)
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
            return "Username not found in database.", (400)

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