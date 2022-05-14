from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import endpoints.transport.transporter as transporter
import helper_functions.sanitation as help

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
                    change_order_state = cur.execute("UPDATE `order` SET `order_status`=%s WHERE id = %s", (state, orderid,))
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

# Change status of item in inventory to pass || not pass quality assurance process
def change_inventory_QA_status(mysql):
    cur = mysql.connection.cursor()
    content = request.get_json(silent=True)
    inventoryid = None
    QAstate = None
    if content:
        inventoryid = help.sanitize_input_numbers(content['inventoryid'])
        QAstate = help.sanitize_input_numbers(content['QAstate'])
    
    if int(QAstate) == 0 or int(QAstate) == 1:
        order = cur.execute("SELECT * FROM `inventory` WHERE id = %s", (inventoryid,))
        if order > 0:
            order = cur.fetchall()
            change_inv_QAstate = cur.execute("UPDATE `inventory` SET `passed_QA`=%s WHERE id = %s", (QAstate, inventoryid,))
            mysql.connection.commit()
            order = cur.execute("SELECT * FROM `inventory` WHERE id = %s", (inventoryid,))
        if order > 0:
            order = cur.fetchall()
            return jsonify(order), 201
        else:
            cur.close()
            return "Bad request", 404
    return "Internal error in database", 500