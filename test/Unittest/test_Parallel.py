import unittest
from Schaltung.Bauelemente.Parallel import Parallel
from Schaltung.Bauelemente.resistor import Resistor
class TestParallel(unittest.TestCase):

    def setUp(self):
        self.R1_obj = Resistor(100)
        self.R2_obj = Resistor(150)

    def test_calcParallel(self):
        # act
        result = Parallel(self.R1_obj, self.R2_obj)
        # assert
        self.assertEqual(60, result.get_ohm())
