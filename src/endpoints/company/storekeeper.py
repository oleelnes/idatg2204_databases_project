from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import endpoints.transport.transporter as transporter

# Adds a new production plan from post with json
def post_production_plan(mysql):
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

# Retrieve orders in the "skis available" state
def get_skis_available_orders(mysql):
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
    return "Internal error in database", 500

# Set order status as storekeeper for spesific orderid to ready to be shipped
# when an order has been filles
def change_order_state(mysql):
    legal = 0
    legalStates = []
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
                    if state == "ready to be shipped":
                        transporter.create_transport_request(mysql, orderid)
                order = cur.execute("SELECT * FROM `order` WHERE id = %s", (orderid,))
                if order > 0:
                    order = cur.fetchall() 
                return jsonify(order), 201
            else:
                cur.close()
                return "Bad request", 404   
        return "Bad request", 404
    return "Internal error in database", 500