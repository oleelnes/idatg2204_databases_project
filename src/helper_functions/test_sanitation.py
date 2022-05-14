import unittest
import helper_functions.sanitation as help

class Test_Sanitation(unittest.TestCase):
    def test_sanitize_input(self):
        self.assertEqual(help.sanitize_input("H@|E.I"), "HEI", "Expected output: HEI")
    
    def test_sanitize_input_numbers(self):
        self.assertEqual(help.sanitize_input_numbers("sad23]¥€"), "23", "Expected output: 23")
    
    def test_sanitize_input_date(self):
        self.assertEqual(help.sanitize_input_date("2%022-02-02@+|"), "2022-02-02", "Expected output: 2022-02-02")

    def test_sanitize_input_letters(self):
        self.assertEqual(help.sanitize_input_letters("324asdE%||"), "asdE", "Expected output: asdE")
