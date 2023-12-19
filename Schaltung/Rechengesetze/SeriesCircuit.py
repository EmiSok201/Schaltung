class SeriesCircuit:

    def calculate_series_circuit(*resistors):
        """Calculate total resistance in series."""
        total_resistance = sum(resistor.ohm for resistor in resistors)
        return total_resistance
