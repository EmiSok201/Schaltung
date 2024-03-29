from Schaltung.Bauelemente.resistor import Resistor


class Parallel(Resistor):
    def __init__(self, r1, r2) -> None:
        super().__init__(self.calcParallel(r1, r2))
        self._r1 = r1
        self._r2 = r2

    def calcParallel(self, r1, r2):
        return 1 / ((1 / r1.get_ohm()) + (1 / r2.get_ohm()))

    def __str__(self):
        return f"parallel({self._r1},{self._r2}):{super().__str__()}"

