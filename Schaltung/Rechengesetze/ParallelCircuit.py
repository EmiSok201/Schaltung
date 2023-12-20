class ParallelCircuit:
    @staticmethod
    def calculate_parallel_circuit(*resistors):
        """Calculate total resistance in parallel."""
        inverse_total = sum(1 / resistor._ohm for resistor in resistors)
        return 1 / inverse_total if inverse_total else float('inf')
