class Resistor:
    def __init__(self, ohm: float) -> None:
        self.ohm = ohm

    def get_ohm(self) -> float:
        """Return ohm value."""
        return self.ohm
