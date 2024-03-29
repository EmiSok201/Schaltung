
class Resistor:
    def __init__(self, ohm: float) -> None:
        self._ohm = ohm

    def get_ohm(self) -> float:
        """Return ohm value."""
        return self._ohm


    def __str__(self):
        return f"{self._ohm} ohm"
