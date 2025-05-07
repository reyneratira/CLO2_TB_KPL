import unittest
from modules.registration import validation_code, defensive_code

class TestRegistration(unittest.TestCase):
    def test_valid_code(self):
        self.assertTrue(validation_code("L01"))

    def test_invalid_code(self):
        self.assertFalse(validation_code("01L"))

    def test_register_success(self):
        customer = defensive_code("Budi", "L02")
        self.assertEqual(customer['name'], "Budi")
        self.assertEqual(customer['service_code'], "L02")

    def test_register_empty_name(self):
        with self.assertRaises(ValueError):
            defensive_code("", "L01")

    def test_register_invalid_code(self):
        with self.assertRaises(ValueError):
            defensive_code("Ayu", "123")