from Bauelemente.resistor import Resistor
from Bauelemente.VoltageSource import VoltageSource
from Rechengesetze.electricalParameters import ElectricalParameters
from Schaltung.Draw_Circuit import DrawCircuit

class Main:
    @staticmethod
    def run():
        # # Initialize resistors
        # resistor1 = Resistor(1)
        # resistor2 = Resistor(5)
        # resistor3 = Resistor(6)
        #
        # # Gesamtwiderstand (In Reihe geschaltet)
        # r1 = resistor1.get_ohm()
        # r2 = resistor2.get_ohm()
        # r3 = resistor3.get_ohm()
        #
        # print(f"Widerstände:")
        # print(f"R1 = {r1} Ohm")
        # print(f"R2 = {r2} Ohm")
        # print(f"R3 = {r3} Ohm")
        #
        # # Calculate total resistances
        # rseries = resistor1.series(resistor2)
        # print(f"Gesamtwiderstand in Reihe: {rseries.get_ohm()} Ohm")
        #
        # rparallel = rseries.parallel(resistor3)
        # print(f"Gesamtwiderstand in Parallel: {rparallel.get_ohm()} Ohm")
        #
        # power_source = PowerSource(30)
        # i0 = power_source.get_ampere()
        #
        # # Bestimmung des Stroms
        # i1 = i0
        # i2 = i0
        # print(f"Ströme:")
        # print(f"I0 = {i0} A")
        # print(f"I1 = {i1} A")
        # print(f"I2 = {i2} A")
        #
        # # Print Ursprungsspannung
        # voltage_source = VoltageSource(30)
        # u0 = voltage_source.get_voltage()
        #
        # print(f"Eingangsspannung:")
        # print(f"U0 = {u0} V")

        # Erste Schaltung
        print(f"Erste Schaltung:")
        u0 = VoltageSource(30)
        r1 = Resistor(250)
        r2 = Resistor(1000)
        r3 = Resistor(3000)

        rparallel = r2.parallel(r3)
        rges = r1.series(rparallel)

        print(f"Widerstände:")
        print(f"R1 = {r1.get_ohm()} Ohm")
        print(f"R2 = {r2.get_ohm()} Ohm")
        print(f"R3 = {r3.get_ohm()} Ohm")
        print(f"R2_R3_Parallel = {rparallel.get_ohm()} Ohm")
        print(f"Gesamtwiderstand R = {rges.get_ohm()} Ohm")

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

        circuit = DrawCircuit()
        circuit.draw()


if __name__ == '__main__':
    main = Main()
    main.run()
