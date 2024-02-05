import unittest
from Schaltung.Bauelemente.PowerSource import PowerSource
class TestPowerSource(unittest.TestCase):

    def setUp(self):
        self.I0 = PowerSource(20)

    def test_get_voltage(self):
        # act
        result = self.I0.get_ampere()
        # assert
        self.assertEqual(20, result)
