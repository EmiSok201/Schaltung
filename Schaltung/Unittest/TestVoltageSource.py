import unittest
from Schaltung.Bauelemente.VoltageSource import VoltageSource
from Schaltung.Bauelemente.resistor import Resistor
class TestVoltageSource(unittest.TestCase):

    def setUp(self):
        self.U = VoltageSource(40)
        self.R1_obj = Resistor(1500)
        self.R2_obj = Resistor(2500)

    def test_get_voltage(self):
        # act
        result = self.U.get_voltage()
        # assert
        self.assertEqual(40, result)

    def test_calcSeries(self):
        # act
        result = self.U.calculate_u(self.R1_obj, self.R2_obj)
        # assert
        self.assertEqual(15, result[0].get_voltage())
        self.assertEqual(25, result[1].get_voltage())
