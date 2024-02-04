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
    def run():

        # Erste Schaltung
        print(f"Erste Schaltung:")
        resistor1 = Resistor(250)
        resistor2 = Resistor(1000)
        resistor3 = Resistor(3000)

        r_parallel = Parallel(resistor2, resistor3)
        r_serie = Series(resistor1, r_parallel)

        print(f"Widerstände:")
        print(f"R1 = {resistor1}")
        print(f"R2 = {resistor2}")
        print(f"R3 = {resistor3}")
        print(f"R2_R3_Parallel = {r_parallel}")
        print(f"Series R = {r_serie}")

        u_0 = VoltageSource(30)
        u_res = u_0.calculate_u(resistor1, r_parallel)
        u_1 = u_res[0]
        u_2 = u_res[1]
        u_3 = u_2

        print(f"Spannungen:")
        print(f"U0 = {u_0.get_voltage()} V")
        print(f"U1 = {u_1.get_voltage()} V")
        print(f"U2 = {u_2.get_voltage()} V")
        print(f"U3 = {u_3.get_voltage()} V")

        # Berechnung Strom
        i_1 = ElectricalParameters(resistor1.get_ohm(), u_1.get_voltage(), 0).calculate_ampere()
        i_2 = ElectricalParameters(resistor2.get_ohm(), u_2.get_voltage(), 0).calculate_ampere()
        i_3 = ElectricalParameters(resistor3.get_ohm(), u_3.get_voltage(), 0).calculate_ampere()

        print(f"Ströme:")
        print(f"I1 = {i_1} A")
        print(f"I2 = {i_2} A")
        print(f"I3 = {i_3} A")

        # Zweite Schaltung
        print(f"Zweite Schaltung:")
        r1 = Resistor(350)
        r2 = Resistor(2000)
        r3 = Resistor(1000)
        r4 = Resistor(400)

        rserie = Series(r3, r4)
        rparallel = Parallel(r2, rserie)
        rges = Series(r1, rparallel)

        print(f"Widerstände:")
        print(f"R1 = {r1}")
        print(f"R2 = {r2}")
        print(f"R3 = {r3}")
        print(f"R3_R4_Series = {rserie}")
        print(f"R2 Parallel R3_R4 = {rparallel}")
        print(f"R Gesamt = {rges}")

        u0 = VoltageSource(20)
        u1 = VoltageSource(20)
        u2 = VoltageSource(10)
        u3 = VoltageSource(15)
        u4 = VoltageSource(35)

        print(f"Spannungen:")
        print(f"U0 = {u0.get_voltage()} V")
        print(f"U1 = {u1.get_voltage()} V")
        print(f"U2 = {u2.get_voltage()} V")
        print(f"U3 = {u3.get_voltage()} V")
        print(f"U4 = {u4.get_voltage()} V")

        # Berechnung Strom
        i1 = ElectricalParameters(resistor1.get_ohm(), u1.get_voltage(), 0).calculate_ampere()
        i2 = ElectricalParameters(resistor2.get_ohm(), u2.get_voltage(), 0).calculate_ampere()
        i3 = ElectricalParameters(resistor3.get_ohm(), u3.get_voltage(), 0).calculate_ampere()
        i4 = ElectricalParameters(r4.get_ohm(), u4.get_voltage(), 0).calculate_ampere()

        print(f"Ströme:")
        print(f"I1 = {i1} A")
        print(f"I2 = {i2} A")
        print(f"I3 = {i3} A")
        print(f"I4 = {i4} A")

        # Plot Erste Schaltung
        Main.visualize_circuit(u_0, [resistor1, r_parallel])
        # Plot Zweite Schaltung
        Main.visualize_circuit(u1, [r1, rparallel, rserie])

    @staticmethod
    def visualize_circuit(voltage_source, resistors):
        visualizer = CircuitVisualizer()
        visualizer.setup_circuit(voltage_source, resistors)
        visualizer.draw()


if __name__ == '__main__':
    main = Main()
    main.run()
    unittest.main()
