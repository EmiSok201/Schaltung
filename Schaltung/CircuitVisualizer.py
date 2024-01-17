import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Schaltung.Bauelemente.Parallel import Parallel


class CircuitVisualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.components = []  # To hold components and their positions
        self.square_size = 4  # Defines the size of the square circuit

    def add_component(self, component_type, label, position, orientation='horizontal'):
        self.components.append((component_type, label, position, orientation))

    def setup_circuit(self, voltage_source, resistors):
        # Add the voltage source on the left middle of the square
        voltage_position = (0, self.square_size / 2)
        self.add_component('voltage_source', 'U', voltage_position)

        # Place resistors in the circuit
        x_offset = 1
        for i, resistor in enumerate(resistors):
            if isinstance(resistor,Parallel):
                position = (x_offset-0.6, self.square_size / 2)
                self.add_component('resistor', f'R{i+1} ({resistor.get_ohm()}Ω)', position, orientation='vertical')
                x_offset += 1
            else:
                position = (x_offset, self.square_size)
                self.add_component('resistor', f'R{i+1} ({resistor.get_ohm()}Ω)', position)
                x_offset += 1

    def draw_resistor(self, position, label, orientation):
        if orientation == 'horizontal':
            self.ax.add_patch(patches.Rectangle((position[0] - 0.2, position[1] - 0.1), 0.4, 0.2, fill=None, edgecolor='black'))
        else:
            self.ax.add_patch(patches.Rectangle((position[0] - 0.1, position[1] - 0.2), 0.2, 0.4, fill=None, edgecolor='black'))
        self.ax.text(position[0], position[1], label, ha='center', va='center')

    def draw_voltage_source(self, position, label):
        self.ax.add_patch(patches.Circle(position, 0.3, fill=None, edgecolor='black'))
        self.ax.text(position[0], position[1], label, ha='center', va='center')

    def draw_wires(self):
        # Draw the square frame of the circuit
        square_coords = [
            (0, 0), (0, self.square_size),
            (self.square_size, self.square_size), (self.square_size, 0),
            (0, 0)
        ]
        self.ax.plot(*zip(*square_coords), 'k-')

        #voltage source is the first component and the first resistor is the second
        if len(self.components) > 1:
            v_source = self.components[0]
            first_resistor = self.components[1]

            # Draw wire from voltage source (U0) to the bottom left corner of the square
            self.ax.plot([v_source[2][0], 0], [v_source[2][1], 0], 'k-')

            # Draw wire from bottom left corner to bottom right corner (following the boundary)
            self.ax.plot([0, first_resistor[2][0]], [0, 0], 'k-')

            # Draw wire up to the first resistor
            self.ax.plot([first_resistor[0][0], first_resistor[0][0]], [0, first_resistor[2][1]], 'k-')

        # Draw the wires for the rest of the components based on their positions
        for i, component in enumerate(self.components[2:], start=2):  # Skip the voltage source and first resistor
            ctype, label, pos, ori = component
            prev_pos = self.components[i - 1][2]
            if ctype == 'resistor':
                if ori == 'horizontal':
                    # Draw wire from the previous component to this resistor
                    self.ax.plot([prev_pos[0], pos[0]], [prev_pos[1], pos[1]], 'k-')
                else:
                    # Draw wire from the top of the square to the parallel resistor
                    self.ax.plot([pos[0], pos[0]], [self.square_size, pos[1]], 'k-')
                    # Draw wire from the parallel resistor to the bottom of the square
                    self.ax.plot([pos[0], pos[0]], [pos[1], 0], 'k-')

                    # Draw wire from the top of the square to the parallel resistor
                    self.ax.plot([pos[0], pos[0]], [self.square_size, pos[1]], 'k-')
                    # Draw wire from the parallel resistor to the bottom of the square
                    self.ax.plot([pos[0], pos[0]], [pos[1], 0], 'k-')



    def draw(self):
        # Draw all components
        for component_type, label, position, orientation in self.components:
            if component_type == 'resistor':
                self.draw_resistor(position, label, orientation)
            elif component_type == 'voltage_source':
                self.draw_voltage_source(position, label)

        # Draw wires
        self.draw_wires()

        # Finalize the plot
        self.show()

    def show(self):
        self.ax.set_xlim(0, self.square_size)
        self.ax.set_ylim(0, self.square_size)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        plt.show()
