class Resistor:

    def __init__(self, resistor, voltage, electricity):
        self.resistor = resistor
        self.voltage = voltage
        self.electricity = electricity

    def calculate_voltage(self):
        voltage = self.resistor * self.electricity
        return voltage

    def calculate_electricity(self):
        electricity = self.voltage / self.resistor
        return electricity

    def calculate_resistor(self):
        resistor = self.voltage / self.electricity
        return resistor
