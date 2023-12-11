class ElectricalParameters:
    
    def __init__(self, ohm, voltage, ampere):
        self.ohm = ohm
        self.voltage = voltage
        self.ampere = ampere

    def calculate_voltage(self):
        voltage = self.ohm * self.ampere
        return voltage

    def calculate_ampere(self):
        ampere = self.voltage / self.ohm
        return ampere


    def calculate_ohm(self):
        ohm = self.voltage / self.ampere
        return ohm