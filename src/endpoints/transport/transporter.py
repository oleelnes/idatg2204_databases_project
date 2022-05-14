from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

# Creates a new transport request from the given orderID input parameter            
def create_transport_request(mysql, orderid):
    cur = mysql.connection.cursor()
    order = cur.execute("SELECT id FROM `order` WHERE id = %s AND order_status = 'ready to be shipped'", (orderid,))
    if order > 0:
        transport = cur.execute("INSERT INTO `shipment` (`order_id`) VALUES (%s)", (orderid,))#"SELECT * FROM `transport`
        mysql.connection.commit()
    cur.close()

# Gets all or a spesific order in the state ready to be shipped
def get_order_info_ready_to_be_shipped(mysql):
    cur = mysql.connection.cursor()
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        content = request.get_json(silent=True)
        orderid = None
        order = None

        if content:
            orderid = content['orderid']

        if orderid:
            order = cur.execute("SELECT * FROM `order` WHERE order_status='ready to be shipped' AND order_id = %s", (orderid,))
            order = cur.fetchall()
        else:
            order = cur.execute("SELECT * FROM `order` WHERE order_status='ready to be shipped'")
            order = cur.fetchall()           
        
        cur.close()
        return jsonify(order), 200
    return "Internal error in database", 500

# Changes the state of a shipment with order id
def change_shipment_state(mysql):
    legal = 0
    legalStates = []
    legalStates.append("in transit")
    legalStates.append("ready for pickup")
    legalStates.append("picked up")

    cur = mysql.connection.cursor()
    if request.method == 'PATCH':
        cur = mysql.connection.cursor()
        content = request.get_json(silent=True)
        orderid = None
        state = None
        order = None
        if content:
            orderid = content['orderid']
            state = content['state']            
        else:
            cur.close()
            return "Bad request", 404   
        
        if state and orderid:
            for val in legalStates:
                if state == val: 
                    legal = 1
            if legal == 1:
                order = cur.execute("SELECT * FROM `shipment` WHERE order_id = %s", (orderid,))
                if order > 0:
                    order = cur.fetchall()
                    change_shipment_state = cur.execute("UPDATE `shipment` SET `state`=%s", (state,))
                    mysql.connection.commit()
                    order = cur.execute("SELECT id FROM `shipment` WHERE order_id = %s", (orderid,))
                    order = cur.fetchall()
                    add_record = cur.execute("INSERT INTO `shipment_record` (`shipment_id`, `state`, `date`) VALUES (%s, %s, CURDATE())", (order[0], state,))
                    mysql.connection.commit()
                order = cur.execute("SELECT * FROM `shipment` WHERE order_id = %s", (orderid,))
                if order > 0:
                    order = cur.fetchall() 
                return jsonify(order), 201
            else:
                cur.close()
                return "Bad request", 404   
    return "Internal error in database", 500