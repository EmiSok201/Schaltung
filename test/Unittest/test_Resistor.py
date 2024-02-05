import unittest
from Schaltung.Bauelemente.resistor import Resistor

class TestResistor(unittest.TestCase):
    def setUp(self):
        self.R = Resistor(500)

    def test_get_Ohm(self):
        # act
        result = self.R.get_ohm()
        # assert
        self.assertEqual(500, result)
