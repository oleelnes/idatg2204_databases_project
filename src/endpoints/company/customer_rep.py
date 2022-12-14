from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import endpoints.transport.transporter as transporter

# Get orders from status as customer rep
def get_order_from_state(mysql):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        state = request.args.get('state')
        if state:
            order = cur.execute("SELECT * FROM `order` WHERE order_status=%s", (state,))
        else: 
            order = cur.execute("SELECT * FROM `order`")
            #cur.close()
            #return "Bad request", 404
        if state != "":
            order = cur.fetchall()
        cur.close()
        return jsonify(order), 200
    return "Internal error in database", 500

# Set order status as customer rep for spesific orderid
def change_order_state(mysql):
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
                    if state == "ready to be shipped":
                        transporter.create_transport_request(mysql, orderid)
                order = cur.execute("SELECT * FROM `order` WHERE id = %s", (orderid,))
                if order > 0:
                    order = cur.fetchall() 
                return jsonify(order), 200
            else:
                cur.close()
                return "Bad request", 404   
        return "Bad request", 404
    return "Internal error in database", 500