from Bauelemente.resistor import Resistor
from Bauelemente.VoltageSource import VoltageSource
from Rechengesetze.electricalParameters import ElectricalParameters
from Schaltung.Bauelemente.Parallel import Parallel
from Schaltung.Bauelemente.Series import Series
from Schaltung.CircuitVisualizer import CircuitVisualizer


class Main:
    @staticmethod
    def run():

        # Erste Schaltung
        print(f"Erste Schaltung:")
        u0 = VoltageSource(30)
        r1 = Resistor(250)
        r2 = Resistor(1000)
        r3 = Resistor(3000)

        rparallel = Parallel(r2, r3)
        rserie = Series(r1, rparallel)

        print(f"Widerstände:")
        print(f"R1 = {r1}")
        print(f"R2 = {r2}")
        print(f"R3 = {r3}")
        print(f"R2_R3_Parallel = {rparallel}")
        print(f"Series R = {rserie}")

        u = u0.calculate_u(r1, rparallel)
        u1 = u[0]
        u2 = u[1]
        u3 = u2

        print(f"Spannungen:")
        print(f"U0 = {u0.get_voltage()} V")
        print(f"U1 = {u1.get_voltage()} V")
        print(f"U2 = {u2.get_voltage()} V")
        print(f"U3 = {u3.get_voltage()} V")

        # Berechnung Strom
        i1 = ElectricalParameters(r1.get_ohm(), u1.get_voltage(), 0).calculate_ampere()
        i2 = ElectricalParameters(r2.get_ohm(), u2.get_voltage(), 0).calculate_ampere()
        i3 = ElectricalParameters(r3.get_ohm(), u3.get_voltage(), 0).calculate_ampere()

        print(f"Ströme:")
        print(f"I1 = {i1} A")
        print(f"I2 = {i2} A")
        print(f"I3 = {i3} A")

        # Zweite Schaltung
        print(f"Zweite Schaltung:")
        u0 = VoltageSource(40)
        r1 = Resistor(100)
        r2 = Resistor(250)
        r3 = Resistor(200)
        r4 = Resistor(100)
        r5 = Resistor(150)

        r4_r5 = Parallel(r4, r5)
        r3_r4_r5 = Parallel(r3, r4_r5)
        r2_r3_r4_r5 = Series(r2, r3_r4_r5)
        r1_r2_r3_r4_r5 = Series(r1, r2_r3_r4_r5)

        print(f"Widerstände:")
        print(f"R1 = {r1}")
        print(f"R2 = {r2}")
        print(f"R3 = {r3}")
        print(f"R4_R5_Parallel = {r4_r5}")
        print(f"R3_Reihe_R4_R5_Parallel = {r3_r4_r5}")
        print(f"R2_Paralle_R3_Reihe_R4_R5_Parallel = {r2_r3_r4_r5}")
        print(f"R_Gesamt = {r1_r2_r3_r4_r5}")

        u1 = 35
        u2 = 40
        u3 = 10
        u4 = 20
        u5 = 20

        print(f"Spannungen:")
        print(f"U0 = {u0.get_voltage()} V")
        print(f"U1 = {u1} V")
        print(f"U2 = {u2} V")
        print(f"U3 = {u3} V")
        print(f"U4 = {u4} V")
        print(f"U5 = {u4} V")

        # Berechnung Strom
        i1 = ElectricalParameters(r1.get_ohm(), u1, 0).calculate_ampere()
        i2 = ElectricalParameters(r2.get_ohm(), u2, 0).calculate_ampere()
        i3 = ElectricalParameters(r3.get_ohm(), u3, 0).calculate_ampere()
        i4 = ElectricalParameters(r4.get_ohm(), u4, 0).calculate_ampere()
        i5 = ElectricalParameters(r5.get_ohm(), u5, 0).calculate_ampere()

        print(f"Ströme:")
        print(f"I1 = {i1} A")
        print(f"I2 = {i2} A")
        print(f"I3 = {i3} A")
        print(f"I4 = {i4} A")
        print(f"I5 = {i5} A")

        # Plot Erste Schaltung
        Main.visualize_circuit(u0, [r1, rparallel, rparallel])
        # Plot Zweite Schaltung
        Main.visualize_circuit(u0, [r1_r2_r3_r4_r5, r2_r3_r4_r5, r3_r4_r5, r4_r5, r4_r5])

    @staticmethod
    def visualize_circuit(voltage_source, resistors):
        visualizer = CircuitVisualizer()
        visualizer.setup_circuit(voltage_source, resistors)
        visualizer.draw()


if __name__ == '__main__':
    Main.run()
