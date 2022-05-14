import unittest
import requests

import main

class Test_Customer(unittest.TestCase):
    CUSTOMER_ENDPOINT = "http://127.0.0.1:5000/customer"
    NEW_ORDER_ENDPOINT = "http://127.0.0.1:5000/customer/orders/new"

    NEW_ORDER_CORRECT_INPUT_JSON = {
        "id":"22112",
        "product_id":"121121",
        "customer_id":"0192189",
        "ski_type":"skate",
        "quantity":"12",
        "total_price": "121",
        "order_status": "new",
        "date": "2022-05-05"
    }
    
    def test_1_check_api(self):
        response = requests.gets(Test_Customer.NEW_ORDER_ENDPOINT)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)

    
    def test_2_new_order_correct_input(self):
        response = requests.post(Test_Customer.NEW_ORDER_ENDPOINT, json=Test_Customer.NEW_ORDER_CORRECT_INPUT_JSON)
        self.assertEqual(response.headers["Content-type"], "application/json")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()