class Resistor:
    def __init__(self, ohm: float) -> None:
        self._ohm = ohm

    def get_ohm(self) -> float:
        """Return ohm value."""
        return self._ohm

    def series(self, r2):
        """Calculate total resistance in series."""
        rtotal = self._ohm + r2.get_ohm()
        return Resistor(rtotal)

    def parallel(self, r2):
        """Calculate total resistance in parallel."""
        rtotal = 1/((1/self._ohm)+(1/r2.get_ohm()))
        return Resistor(rtotal)
