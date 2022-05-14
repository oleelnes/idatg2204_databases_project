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