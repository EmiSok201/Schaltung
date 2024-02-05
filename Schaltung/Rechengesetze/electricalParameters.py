class ElectricalParameters:

    # - Berechnung der einzelnen Parameter
    def __init__(self, ohm, voltage, ampere):
        self.ohm = ohm
        self.voltage = voltage
        self.ampere = ampere

    # - Berechnung der Spannung
    def calculate_voltage(self):
        voltage = self.ohm * self.ampere
        return voltage

    # - Berechnung des Stroms
    def calculate_ampere(self):
        ampere = self.voltage / self.ohm
        return ampere

    # - Berechnung des Widerstands
    def calculate_ohm(self):
        ohm = self.voltage / self.ampere
        return ohm

    @staticmethod  # Calculate the currents I based on the resistances Ohm and voltages
    def calculate_currents(resistors, voltages):
        currents = {}
        for label, (resistor, voltage) in enumerate(zip(resistors, voltages), start=1):
            current = ElectricalParameters(resistor.get_ohm(), voltage.get_voltage(), 0).calculate_ampere()
            currents[f"I{label}"] = current
        return currents
