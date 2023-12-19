from Bauelemente.resistor import Resistor
from Bauelemente.PowerSource import PowerSource
from Bauelemente.VoltageSource import VoltageSource
from Rechengesetze.SeriesCircuit import SeriesCircuit
from Rechengesetze.ParallelCircuit import ParallelCircuit
from Rechengesetze.VoltageDivider import VoltageDivider


class Main:
    @staticmethod
    def run():
        # Initialize resistors
        resistor1 = Resistor(20)
        resistor2 = Resistor(30)
        resistor3 = Resistor(5)

        # Gesamtwiderstand (In Reihe geschaltet)
        r1 = resistor1.get_ohm()
        r2 = resistor2.get_ohm()
        r3 = resistor3.get_ohm()

        print(f"Widerstände:")
        print(f"R1 = {r1} Ohm")
        print(f"R2 = {r2} Ohm")
        print(f"R3 = {r3} Ohm")

        # Calculate total resistances using class
        total_series_resistance = SeriesCircuit.calculate_series_circuit(resistor1, resistor2, resistor3)
        total_parallel_resistance = ParallelCircuit.calculate_parallel_circuit(resistor1, resistor2, resistor3)

        # Print total resistances
        print(f"Gesamtwiderstand in Reihe: {total_series_resistance} Ohm")
        print(f"Gesamtwiderstand in Parallel: {total_parallel_resistance} Ohm")

        power_source = PowerSource(30)
        i0 = power_source.get_ampere()

        # Bestimmung des Stroms
        i1 = i0
        i2 = i0
        print(f"Ströme:")
        print(f"I0 = {i0} A")
        print(f"I1 = {i1} A")
        print(f"I2 = {i2} A")

        # Print Ursprungsspannung
        voltage_source = VoltageSource(30)
        u0 = voltage_source.get_voltage()

        print(f"Eingangsspannung:")
        print(f"U0 = {u0} V")

        # Berechnung der Teilspannungen
        u = VoltageDivider.calculate_u(u0, resistor1, resistor2, resistor3)
        print(f"Berechnete Teilspannungen:")
        print(f"U = {u} V")


if __name__ == '__main__':
    main = Main()
    main.run()
