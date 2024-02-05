
class Resistor:
    def __init__(self, ohm: float) -> None:
        if ohm < 0:
            raise ValueError("Der Widerstand darf nicht negativ sein.")
        self._ohm = ohm

    def get_ohm(self) -> float:
        """Return ohm value."""
        return self._ohm

    def __str__(self):
        return f"{self._ohm} ohm"
    @staticmethod
    def print(prefix, *resistors):
        print(f"{prefix} Widerstände:")
        for idx, resistor in enumerate(resistors, 1):
            print(f"R{idx} = {resistor}")
