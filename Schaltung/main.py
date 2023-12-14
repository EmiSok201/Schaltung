from Bauelemente.resistor import Resistor
from Rechengesetze.circuitCalculation import CircuitCalculation
from Schaltung.Rechengesetze.voltageDivider import VoltageDivider
from Bauelemente.PowerSource import PowerSource
from Bauelemente.VoltageSource import VoltageSource

class Main:
    @staticmethod
    def run():

        # Initialize resistors
        resistor1 = Resistor(20)
        resistor2 = Resistor(30)
        resistor3 = Resistor(5)

        # Gesamtwiderstand (In Reihe geschaltet)
        #  circuitCalc =
        #  circuit = CircuitCalculation(resistor, resistor2)
        #  resistor_ges = circuit.calculate_series_circuit
        print("R1 = ", resistor1, "Ohm")
        print("R2 = ", resistor2, "Ohm")
        print("R3 = ", resistor3, "Ohm")
        #        print("Gesamtwiderstand = ", resistor_ges, "Ohm")
        # Calculate total resistances using CircuitCalculation class
        total_series_resistance = CircuitCalculation.calculate_series_circuit(resistor1, resistor2, resistor3)
        total_parallel_resistance = CircuitCalculation.calculate_parallel_circuit(resistor1, resistor3)

        # Print total resistances
        print(f"Total Resistance in Series: {total_series_resistance} Ohm")
        print(f"Total Resistance in Parallel: {total_parallel_resistance} Ohm")


        power_source = PowerSource(30)
        i0 = power_source.get_ampere()

        voltage_source = VoltageSource(30)
        u0 = voltage_source.get_voltage()

        # Reihenschaltung von r1 und r2



        # Bestimmung des Stroms
        i1 = i0
        i2 = i0

        print("I1 =", i1, "A")
        print("I2 =", i2, "A")

       # Print Ursprungsspannung
        print("V0 =", u0, "V Eingangsspannung")

        print("Berechnete Ausgangsspannungen:")
        # Berechnung der Teilspannungen
#        u1 = VoltageDivider(r1, r2, u0).calculate_u1()
#        print("U1 =", u1, "V")

#        u2 = VoltageDivider(r1, r2, u0).calculate_u2()
#        print("U2 =", u2, "V")

if __name__ == '__main__':
    main = Main()
    main.run()
