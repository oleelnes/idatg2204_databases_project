from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import helper_functions.sanitation as help

# Adds a new production plan from post with json
def post_production_plan(mysql):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        content = request.get_json()
        if content:
            week = help.sanitize_input_numbers(content['startweek'])
            productid = help.sanitize_input_numbers(content['productid'])
            day = help.sanitize_input_numbers(content['day'])
            type = help.sanitize_input(content['type'])
            productionAmount = help.sanitize_input_numbers(content['productionAmount'])
            manufacturer_id = help.sanitize_input_numbers(content['manufacturerid'])
        else:
            cur.close()
            return "Bad request", 404

        if week != "" and int(week) < 50 and int(week) > 0 and productid != "" and day != "" and type != "" and productionAmount != "" and manufacturer_id != "":
            weeks = range(4)
            for i in weeks:
                tmp = cur.execute("SELECT week_number FROM `production_plan` WHERE week_number = %s", (week,))
                tmp = cur.fetchall()
                if tmp == None:
                    plan = cur.execute("INSERT INTO `production_plan` (`week_number`, `manufacturer_id`) VALUES (%s, %s)", (week, manufacturer_id,))
                    mysql.connection.commit()
                    typeData = cur.execute("INSERT INTO `production_type` \
                        (`production_week_number`, `product_id`, `day`, `type`, `production_amount`) \
                        VALUES (%s, %s, %s, %s, %s)", (week, productid, day, type, productionAmount,))
                    mysql.connection.commit()
                    week += 1

            prodplan = cur.execute("SELECT * FROM `production_type` WHERE production_week_number BETWEEN %s AND %s", (week - 4, week,))
            if prodplan > 0:
                prodplan = cur.fetchall()
                cur.close()
                return jsonify(prodplan), 201
        else:
            cur.close()
            return "Bad request", 404   
    else: 
        return "Wrong method. Only POST is supported.", 405
    return "Internal error in database", 500 