class VoltageDivider:

    def __init__(self, ohm, ohm2, volt):
        self.ohm = ohm
        self.ohm2 = ohm2
        self.volt = volt

    def calculate_u1(self):
        resistor_ges = self.ohm + self.ohm2
        u1 = self.volt * (self.ohm / resistor_ges)
        return u1

    def calculate_u2(self):
        resistor_ges = self.ohm + self.ohm2
        u2 = self.volt * (self.ohm2 / resistor_ges)
        return u2

