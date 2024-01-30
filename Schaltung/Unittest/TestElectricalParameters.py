import unittest
from Schaltung.Rechengesetze.electricalParameters import ElectricalParameters
from Schaltung.Bauelemente.resistor import Resistor
from Schaltung.Bauelemente.PowerSource import PowerSource
from Schaltung.Bauelemente.VoltageSource import VoltageSource
class TestElectricalParameters(unittest.TestCase):

    def setUp(self):
        self.R_obj = Resistor(100)
        self.I_obj = PowerSource(20)
        self.U_obj = VoltageSource(10)

    def test_calculate_voltage(self):
        # act
        result = ElectricalParameters(self.R_obj.get_ohm(), 0, self.I_obj.get_ampere()).calculate_voltage()
        # assert
        self.assertEqual(2000, result)

    def test_calculate_ampere(self):
        # act
        result = ElectricalParameters(self.R_obj.get_ohm(), self.U_obj.get_voltage(), 0).calculate_ampere()
        # assert
        self.assertEqual(0.1, result)

    def test_calculate_ohm(self):
        # act
        result = ElectricalParameters(0, self.U_obj.get_voltage(), self.I_obj.get_ampere()).calculate_ohm()
        # assert
        self.assertEqual(0.5, result)
