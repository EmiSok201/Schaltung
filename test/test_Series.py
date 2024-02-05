import unittest
from Schaltung.Bauelemente.Series import Series
from Schaltung.Bauelemente.Resistor import Resistor
class TestSeries(unittest.TestCase):

    def setUp(self):
        self.R1_obj = Resistor(100)
        self.R2_obj = Resistor(350)

    def test_calcSeries(self):
        # act
        result = Series(self.R1_obj, self.R2_obj)
        # assert
        self.assertEqual(450, result.get_ohm())
