import unittest
import requests

class Test_Public(unittest.TestCase):
    PUBLIC_ENDPOINT = "http://127.0.0.1:5000/public"
    CORRECT_INPUT = "?modelname=race pro&size=142"

    def test_1_get_skis(self):
        response = requests.get(Test_Public.PUBLIC_ENDPOINT + Test_Public.CORRECT_INPUT)
        self.assertEqual(response.headers["Content-type"], "application/json")
        self.assertEqual(response.status_code, 200)
