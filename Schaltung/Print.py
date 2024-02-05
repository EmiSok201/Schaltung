class Print:
    def __init__(self) -> None:
        pass

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
