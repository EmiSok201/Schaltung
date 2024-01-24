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
        r4 = Resistor(500)
        rparallel = Parallel(r2, r3)
        rserie = Series(r3, rparallel)
        rges = Series(r1, rparallel)


        print(f"Widerstände:")
        print(f"R1 = {r1}")
        print(f"R2 = {r2}")
        print(f"R3 = {r3}")
        print(f"R2_R3_Parallel = {rparallel}")
        print(f"Gesamtwiderstand R = {rges}")
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

        Main.visualize_circuit(u0, [r1, rserie, rparallel, r2, rparallel])
       # Main.visualize_circuit(u0, [r4, rparallel, rparallel])


    @staticmethod
    def visualize_circuit(voltage_source, resistors):
        visualizer = CircuitVisualizer()
        visualizer.setup_circuit(voltage_source, resistors)
        visualizer.draw()

if __name__ == '__main__':
    Main.run()
