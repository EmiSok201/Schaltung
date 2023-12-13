from __future__ import annotations


class Resistor:

    # - Initialisierung der Widerstände
    def __init__(self, ohm: float) -> None:
        self._ohm = ohm

    def get_ohm(self) -> float:
        return self._ohm

    def series(self, resistor2: Resistor) -> Resistor:
        return Resistor(self.get_ohm() + resistor2.get_ohm())
