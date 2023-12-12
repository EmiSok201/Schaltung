from Bauelemente.Resistor import Resistor
from Bauelemente.VoltageDivider import VoltageDivider
from Bauelemente.PowerSource import PowerSource
from Bauelemente.VoltageSource import VoltageSource

class Main:

    @staticmethod
    def run():

        # Initialisierung der Bauelemente
        resistor = Resistor(5)
        r1 = resistor.get_resistor()
        resistor2 = Resistor(10)
        r2 = resistor2.get_resistor()
        power_source = PowerSource(30)
        u0 = power_source.get_ampere()
        voltage_source = VoltageSource(25)
        i0 = voltage_source.get_voltage()

        # Reihenschaltung von r1 und r2

        # Berechnung Gesamtwiderstand
        resistor_ges = r1 + r2
        print("Gesamtwiderstand = ", resistor_ges, "Ohm")

        # Berechnung der Teilspannungen
        u1 = VoltageDivider(r1, r2, u0).calculate_u1()
        print("U1 =", u1, "V")

        u2 = VoltageDivider(r1, r2, u0).calculate_u2()
        print("U2 =", u2, "V")

        # Bestimmung des Stroms
        i1 = i0
        i2 = i0
        print("I1 =", i1, "A")
        print("I2 =", i2, "A")


if __name__ == '__main__':
    main = Main()
    main.run()
