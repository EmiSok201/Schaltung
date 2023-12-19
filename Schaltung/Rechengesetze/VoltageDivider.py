class VoltageDivider:

    @staticmethod
    def calculate_u(volt, *resistors):
        """Calculate partial voltages."""
        resistor_ges = sum(resistor.ohm for resistor in resistors)
        voltages = [volt * (resistor.ohm / resistor_ges) for resistor in resistors]
        return voltages
