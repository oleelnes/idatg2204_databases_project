from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

from main import createHashedPassword, createSalt

def place_order(mysql):
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

def delete_order(mysql):
    if request.method == 'DELETE':
        cur = mysql.connection.cursor()
        id = request.args.get('id')

        if id is None:
            return "Id needs to be passed.", 400

        delete = cur.execute("DELETE FROM `order` WHERE id=%s", (id,))

        mysql.connection.commit()
        cur.close()
        return "successfully deleted order with id " + id, 200
    else:
        return "Wrong method. Only GET is supported.", 405

def get_order_by_id(mysql):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        id = request.args.get('order_id')
        if id is None:
            return "Id must be entered as a key.", 400
            
        retrieved_order = cur.execute("SELECT * FROM `order` WHERE `id`=%s", (id,))

        if retrieved_order == 0:
            return "There exists no order with id " + id + " in the database.", 400

        retrieved_order = cur.fetchall()
        cur.close()
        return jsonify(retrieved_order), 200
    else:
        return "Wrong method. Only GET is supported.", 405

def get_orders_since(mysql):
    if request.method == 'GET':
        cur = mysql.connection.cursor()

        date = request.args.get('date')

        if date is None:
            return "Date must be entered as a key.", 400
        
        orders = cur.execute("SELECT * FROM `order` WHERE `date` BETWEEN %s AND CURDATE() ORDER BY date asc", (date,))
        orders = cur.fetchall()
        cur.close()

        return jsonify(orders)
    else:
        return "Wrong method. Only GET is supported.", 405

def get_production_plan_summary(mysql):
    if request.method == 'GET':
        cur = mysql.connection.cursor()

        orders = cur.execute("SELECT * FROM `production_plan` WHERE week_number BETWEEN WEEK(CURDATE()) \
            AND WEEK(CURDATE())+4 GROUP BY week_number ORDER BY week_number asc")
        orders = cur.fetchall()

        cur.close()
        return jsonify(orders), 200
    else:
        return "Wrong method. Only GET is supported.", 405
        

