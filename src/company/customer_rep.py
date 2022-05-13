from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

def get_order(x,y):
    print("mong")
    if request.method == 'GET':
        cur = x.connection.cursor()
        
    return "Error in database", 500