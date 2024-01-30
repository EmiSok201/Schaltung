import unittest
from Schaltung.Bauelemente.resistor import Resistor
class TestResistor(unittest.TestCase):

    def setUp(self):
        self.r = Resistor(1500)

    def test_get_voltage(self):
        # act
        result = self.r.get_ohm()
        # assert
        self.assertEqual(1500, result)
