import unittest
from modules.registration import services_code_validation, create_valid_customer_data

class TestRegistration(unittest.TestCase):
    def test_valid_code(self):
        self.assertTrue(services_code_validation("L01"))

    def test_invalid_code(self):
        self.assertFalse(services_code_validation("01L"))

    def test_register_success(self):
        customer = create_valid_customer_data("Budi", "L02")
        self.assertEqual(customer['name'], "Budi")
        self.assertEqual(customer['services_code'], "L02")

    def test_register_empty_name(self):
        with self.assertRaises(ValueError):
            create_valid_customer_data("", "L01")

    def test_register_invalid_code(self):
        with self.assertRaises(ValueError):
            create_valid_customer_data("Ayu", "123")