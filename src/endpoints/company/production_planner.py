from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

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