class VoltageDivider:

    @staticmethod
    def calculate_u(volt, *resistors):
        """Calculate partial voltages."""
        resistor_ges = sum(resistor._ohm for resistor in resistors)
        voltages = [volt * (resistor._ohm / resistor_ges) for resistor in resistors]
        return voltages
