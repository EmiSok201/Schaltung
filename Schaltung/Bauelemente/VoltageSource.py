class VoltageSource:

    # - Initialisierung der Spannungsquelle
    def __init__(self, volt):
        self._volt = volt

    def get_voltage(self):
        volt = self._volt
        return volt

    def calculate_u(self, *resistors):
        """Calculate partial voltages."""
        resistor_ges = sum(resistor._ohm for resistor in resistors)
        u = [self._volt * (resistor._ohm / resistor_ges) for resistor in resistors]

        ulist = []
        for i in range(len(u)):
            ulist.append(VoltageSource(u[i]))

        return ulist
