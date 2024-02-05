from Bauelemente.resistor import Resistor
from Bauelemente.VoltageSource import VoltageSource
from Rechengesetze.electricalParameters import ElectricalParameters
from Schaltung.Bauelemente.Parallel import Parallel
from Schaltung.Bauelemente.Series import Series
from Schaltung.CircuitVisualizer import CircuitVisualizer
from Schaltung.Unittest.TestSeries import TestSeries
from Schaltung.Unittest.TestParallel import TestParallel
from Schaltung.Unittest.TestResistor import TestResistor
from Schaltung.Unittest.TestPowerSource import TestPowerSource
from Schaltung.Unittest.TestVoltageSource import TestVoltageSource
from Schaltung.Unittest.TestElectricalParameters import TestElectricalParameters
import unittest

class Main:
    @staticmethod
    def print_resistors(prefix, *resistors):
        print(f"{prefix} Widerstände:")
        for idx, resistor in enumerate(resistors, 1):
            print(f"R{idx} = {resistor}")

    @staticmethod
    def print_voltages(prefix, **voltages):
        print(f"{prefix} Spannungen:")
        for label, voltage in voltages.items():
            print(f"{label} = {voltage.get_voltage()} V")

    @staticmethod
    def print_currents(prefix, **currents):
        print(f"{prefix} Ströme:")
        for label, current in currents.items():
            print(f"{label} = {current} A")

    @staticmethod
    def calculate_currents(resistors, voltages):
        currents = {}
        for label, (resistor, voltage) in enumerate(zip(resistors, voltages), start=1):
            current = ElectricalParameters(resistor.get_ohm(), voltage.get_voltage(), 0).calculate_ampere()
            currents[f"I{label}"] = current
        return currents

    @staticmethod
    def run():
        # Erste Schaltung
        resistor1 = Resistor(250)
        resistor2 = Resistor(1000)
        resistor3 = Resistor(3000)

        r_parallel = Parallel(resistor2, resistor3)
        r_serie = Series(resistor1, r_parallel)

        Main.print_resistors("Erste Schaltung", resistor1, resistor2, resistor3, r_parallel, r_serie)

        u_0 = VoltageSource(30)
        u_res = u_0.calculate_u(resistor1, r_parallel)
        u_1, u_2 = u_res[0], u_res[1]
        u_3 = u_2

        Main.print_voltages("Erste Schaltung", U0=u_0, U1=u_1, U2=u_2, U3=u_3)

        currents_erste_schaltung = Main.calculate_currents([resistor1, resistor2, resistor3], [u_1, u_2, u_3])
        Main.print_currents("Erste Schaltung", **currents_erste_schaltung)

        # Zweite Schaltung
        r1 = Resistor(200)
        r2 = Resistor(300)
        r3 = Resistor(500)
        r4 = Resistor(400)

        rserie = Series(r3, r4)
        rparallel = Parallel(r2, rserie)
        rges = Series(r1, rparallel)

        Main.print_resistors("Zweite Schaltung", r1, r2, r3, r4, rserie, rparallel, rges)

        u0 = VoltageSource(20)
        u1 = VoltageSource(18.31)
        u2 = VoltageSource(11.68)
        u3 = u4 = u2

        # Print voltages
        Main.print_voltages("Zweite Schaltung", U0=u0, U1=u1, U2=u2, U3=u3, U4=u4)

        currents_zweite_schaltung = Main.calculate_currents([r1, r2, r3, r4], [u1, u2, u3, u4])
        Main.print_currents("Zweite Schaltung", **currents_zweite_schaltung)

        # Visualization
        Main.visualize_circuit(u_0, [resistor1, r_parallel])
        Main.visualize_circuit(u0, [r1, rparallel, r4])

    @staticmethod
    def visualize_circuit(voltage_source, resistors):
        visualizer = CircuitVisualizer()
        visualizer.setup_circuit(voltage_source, resistors)
        visualizer.draw()

if __name__ == '__main__':
    main = Main()
    main.run()
    unittest.main()
