import unittest
import requests


class Test_Production_Planner(unittest.TestCase):
    PROD_ENDPOINT = "http://127.0.0.1:5000/productionplanner"
    LOGIN_URL = "http://127.0.0.1:5000/authentication/login"

    LOGIN_CRED = {
        "username":"prodplan1",
        "password": "prod1"
    }

    CORRECT_JSON = {
        "startweek":17,
        "productid":2,
        "day":"1",
        "type":"skate",
        "productionAmount":"100",
        "manufacturerid":"200000"
}

    def login():
        response = requests.post(Test_Production_Planner.LOGIN_URL, json=Test_Production_Planner.LOGIN_CRED)

    def test_1_post_production_plan(self):
        Test_Production_Planner.login()
        response = requests.post(Test_Production_Planner.PROD_ENDPOINT, json=Test_Production_Planner.CORRECT_JSON)
        self.assertEqual(response.headers["Content-type"], "application/json")
        self.assertEqual(response.status_code, 201)