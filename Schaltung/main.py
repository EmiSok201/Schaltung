from Bauelemente.Resistor import Resistor
from Schaltung.Rechengesetze.VoltageDivider import VoltageDivider
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
        i0 = power_source.get_ampere()

        voltage_source = VoltageSource(30)
        u0 = voltage_source.get_voltage()

        # Reihenschaltung von r1 und r2

        # Gesamtwiderstand (In Reihe geschaltet)
        resistor_ges = r1 + r2
        print("R1 = ", r1, "Ohm")
        print("R2 = ", r2, "Ohm")
        print("Gesamtwiderstand = ", resistor_ges, "Ohm")

        # Bestimmung des Stroms
        i1 = i0
        i2 = i0

        print("I1 =", i1, "A")
        print("I2 =", i2, "A")

       # Print Ursprungsspannung
        print("V0 =", u0, "V Eingangsspannung")

        print("Berechnete Ausgangsspannungen:")
        # Berechnung der Teilspannungen
        u1 = VoltageDivider(r1, r2, u0).calculate_u1()
        print("U1 =", u1, "V")

        u2 = VoltageDivider(r1, r2, u0).calculate_u2()
        print("U2 =", u2, "V")

if __name__ == '__main__':
    main = Main()
    main.run()
