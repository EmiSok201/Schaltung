import unittest
from Schaltung.Bauelemente.resistor import Resistor

class TestResistor(unittest.TestCase):
    def test_resistor_values(self):
        test_cases = [
            (1500, 'positive'),  # Expected to pass
            (-10, 'negative')    # Expected to fail
        ]

        for resistance_value, description in test_cases:
            with self.subTest(resistance_value=resistance_value, description=description):
                if description == 'negative':
                    with self.assertRaises(ValueError, msg=f"Resistor value {resistance_value} should raise ValueError"):
                        Resistor(resistance_value)
                else:
                    try:
                        resistor = Resistor(resistance_value)
                        self.assertEqual(resistor.get_ohm(), resistance_value, f"Expected {resistance_value} ohms.")
                    except ValueError as e:
                        self.fail(f"Initialization with {resistance_value} ohms should not raise ValueError. Error: {str(e)}")

