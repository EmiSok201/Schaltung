class Resistor:

    def __init__(self, resistor, voltage, ampere):
        self.resistor = resistor
        self.voltage = voltage
        self.ampere = ampere

    def calculate_voltage(self):
        voltage = self.resistor * self.ampere
        return voltage

    def calculate_ampere(self):
        ampere = self.voltage / self.resistor
        return ampere

    def calculate_resistor(self):
        resistor = self.voltage / self.ampere
        return resistor
