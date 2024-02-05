from Bauelemente.Resistor import Resistor
from Bauelemente.VoltageSource import VoltageSource
from Rechengesetze.electricalParameters import ElectricalParameters
from Schaltung.Bauelemente.Parallel import Parallel
from Schaltung.Bauelemente.Series import Series
from Schaltung.CircuitVisualizer import CircuitVisualizer
from Schaltung.Print import Print


class Main:

    def run(self):
        # First circuit
        resistor1 = Resistor(100)
        resistor2 = Resistor(1000)
        resistor3 = Resistor(3000)

        r_parallel = Parallel(resistor2, resistor3)
        r_serie = Series(resistor1, r_parallel)

        Resistor.print("Erste Schaltung", resistor1, resistor2, resistor3, r_parallel, r_serie)

        u_0 = VoltageSource(30)
        u_res = u_0.calculate_u(resistor1, r_parallel)
        u_1, u_2 = u_res[0], u_res[1]
        u_3 = u_2

        Print.print_voltages("Erste Schaltung", U0=u_0, U1=u_1, U2=u_2, U3=u_3)

        currents_erste_schaltung = ElectricalParameters.calculate_currents([resistor1, resistor2, resistor3],
                                                                           [u_1, u_2, u_3])
        Print.print_currents("Erste Schaltung", **currents_erste_schaltung)

        # Visualization
        Main.visualize_circuit(u_0, [resistor1, r_parallel, resistor3, r_parallel])

    @staticmethod
    def visualize_circuit(voltage_source, resistors):
        visualizer = CircuitVisualizer()
        visualizer.setup_circuit(voltage_source, resistors)
        visualizer.draw()


if __name__ == '__main__':
    main = Main()
    main.run()
