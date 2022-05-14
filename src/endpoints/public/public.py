from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import helper_functions.sanitation as help


def get_skis(mysql):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        modelname = help.sanitize_input(request.args.get('modelname'))
        size = help.sanitize_input_numbers(request.args.get('size'))
        
        if modelname and size:
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo \
            FROM `product` \
            WHERE model = %s AND size = %s", (modelname,size,))
        elif modelname:
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo \
            FROM `product` \
            WHERE model = %s", (modelname,))
        elif size:
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo \
            FROM `product` \
            WHERE size = %s", (size,))
        else:        
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo FROM `product`")
        if skis > 0:
            skis = cur.fetchall()
        cur.close()
        return jsonify(skis), 200
    return "Internal error in database", 500