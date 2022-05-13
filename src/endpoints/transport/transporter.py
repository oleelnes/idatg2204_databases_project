from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

# Creates a new transport request from the given orderID input parameter            
def create_transport_request(mysql,orderid):
    cur = mysql.connection.cursor()
    order = cur.execute("SELECT id FROM `order` WHERE id = %s AND order_status = 'fulfilled'", (orderid,))
    if order > 0:
        transport = cur.execute("INSERT INTO `shipment` (`order_id`) VALUES (%s)", (orderid,))#"SELECT * FROM `transport`
        mysql.connection.commit()
    cur.close()