from Bauelemente.Resistor import Resistor
from Bauelemente.PowerSource import PowerSource
from Bauelemente.VoltageSource import VoltageSource

class Main:

    @staticmethod
    def run():

        resistor = Resistor(5, 10, 10)
        power_source = PowerSource(20)
        voltage_source = VoltageSource(25)

