from Schaltung.Bauelemente.resistor import Resistor


class Series(Resistor):
    def __init__(self, r1: Resistor, r2: Resistor) -> None:
        super().__init__(self.calcSeries(r1, r2))
        self._r1 = r1
        self._r2 = r2

    def calcSeries(self, r1, r2):
        return r1.get_ohm() + r2.get_ohm()

    def __str__(self):
        return f"series({self._r1},{self._r2}):{super().__str__()}"
