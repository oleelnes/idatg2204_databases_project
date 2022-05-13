import unittest
import requests

class test_customer(unittest.TestCase):
    CUSTOMER_ENDPOINT = "http://127.0.0.1:5000/customer"
    NEW_ORDER = CUSTOMER_ENDPOINT + "/orders/new"

    def test_1_check_api(self):
        response = requests.gets(test_customer.NEW_ORDER)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)