class CircuitCalculation:
    @staticmethod
    def calculate_series_circuit(*resistors):
        """Calculate total resistance in series."""
        total_resistance = sum(resistor.ohm for resistor in resistors)
        return total_resistance

    @staticmethod
    def calculate_parallel_circuit(*resistors):
        """Calculate total resistance in parallel."""
        inverse_total = sum(1 / resistor.ohm for resistor in resistors)
        return 1 / inverse_total if inverse_total else float('inf')
