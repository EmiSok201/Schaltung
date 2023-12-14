from __future__ import annotations


class Resistor:
    def __init__(self, ohm: float) -> None:
        self.ohm = ohm

    def __add__(self, other: Resistor) -> Resistor:
        """Combine resistors in series."""
        if not isinstance(other, Resistor):
            raise ValueError("Can only add another Resistor.")
        return Resistor(self.ohm + other.ohm)

    def __mul__(self, other: Resistor) -> Resistor:
        """Combine resistors in parallel."""
        if not isinstance(other, Resistor):
            raise ValueError("Can only multiply with another Resistor.")
        return Resistor((self.ohm * other.ohm) / (self.ohm + other.ohm))


    #
    # # - Initialisierung der Widerstände
    # def __init__(self, ohm: float) -> None:
    #     self._ohm = ohm
    #
    # def get_ohm(self) -> float:
    #     return self._ohm
    #
    # def series(self, resistor2: Resistor) -> Resistor:
    #     return Resistor(self.get_ohm() + resistor2.get_ohm())
