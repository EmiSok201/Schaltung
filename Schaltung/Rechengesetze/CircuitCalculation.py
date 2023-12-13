class CircuitCalculation:

    def __init__(self, resistor1, resistor2):
        self.resistor1 = resistor1
        self.resistor2 = resistor2

    def calculate_series_circuit(self):

        resistor = self.resistor1 + self.resistor2

        return resistor


def calculate_parallel_circuit(self):
    resistor = (self.resistor1 * self.resistor2) / (self.resistor1 + self.resistor2)
    return resistor

