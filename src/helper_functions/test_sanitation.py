import unittest
import helper_functions.sanitation as help

class TestSanitation(unittest.TestCase):
    def test_sanitize_input(self):
        self.assertEqual(help.sanitize_input("H2@|E.I"), "HEI", "Should be: HEI")

#if __name__ == '__sanitation__':
#    unittest.sanitation()