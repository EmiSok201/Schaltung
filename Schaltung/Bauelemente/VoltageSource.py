class VoltageSource:

    # - Initialisierung der Spannungsquelle
    def __init__(self, voltage):
        self.voltage = voltage

    def get_voltage(self):
        voltage = self.voltage
        return voltage