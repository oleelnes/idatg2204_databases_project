import unittest
import requests

class Test_Customer_Rep(unittest.TestCase):
    CUSTOMER_REP_ORDER_ENDPOINT = "http://127.0.0.1:5000/customerrep/orders"
    CUSTOMER_REP_SET_ORDER_STATUS = "http://127.0.0.1:5000/customerrep/setorderstatus"
    LOGIN_URL = "http://127.0.0.1:5000/authentication/login"

    CORRECT_INPUT_JSON_CHANGE_STATUS = {
        "orderid": "1",
        "state": "open"
    }

    LOGIN_CRED = {
        "username":"customerrep1",
        "password": "cust1"
}

    def login():
        response = requests.post(Test_Customer_Rep.LOGIN_URL, json=Test_Customer_Rep.LOGIN_CRED)

    def test_1_check_api(self):
        Test_Customer_Rep.login()
        response = requests.get(Test_Customer_Rep.CUSTOMER_REP_ORDER_ENDPOINT)
        self.assertEqual(response.headers["Content-type"], "application/json")
        self.assertEqual(response.status_code, 200)

    def test_2_get_order(self):
        Test_Customer_Rep.login()
        response = requests.get(Test_Customer_Rep.CUSTOMER_REP_ORDER_ENDPOINT + "?state=new")
        self.assertEqual(response.headers["Content-type"], "application/json")
        self.assertEqual(response.status_code, 200)

    def test_3_set_order_status(self):
        Test_Customer_Rep.login()
        response = requests.patch
        (Test_Customer_Rep.CUSTOMER_REP_SET_ORDER_STATUS, json=Test_Customer_Rep.CORRECT_INPUT_JSON_CHANGE_STATUS)
        self.assertEqual(response.headers["Content-type"], "application/json")
        self.assertEqual(response.status_code, 200)