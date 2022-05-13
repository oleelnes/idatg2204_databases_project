from flask import Flask, request, jsonify
from flask_mysqldb import MySQL


def get_skis(mysql):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        modelname = request.args.get('modelname')
        if modelname:
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo \
            FROM `product` \
            WHERE model = %s", (modelname,))
        else:        
            skis = cur.execute("SELECT model, type, size, description, MSRPP ,url_photo FROM `product`")
        if skis > 0:
            skis = cur.fetchall()
        cur.close()
        return jsonify(skis), 200
    return "Error in db", 500