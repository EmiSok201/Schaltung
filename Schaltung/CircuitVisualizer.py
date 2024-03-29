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

        # Calculate the spacing for resistors
        spacing = self.square_size / (len(resistors) + 1)

        # Place resistors in the circuit
        for i, resistor in enumerate(resistors):
            x_position = (i + 1) * spacing
            if isinstance(resistor, Parallel):
                # Place parallel resistors vertically on the right
                position = (x_position, self.square_size / 2)
                orientation = 'vertical'
            else:
                # Place other resistors horizontally along the top
                position = (x_position, self.square_size)
                orientation = 'horizontal'
            self.add_component('resistor', f'R{i+1} ({resistor.get_ohm()}Ω)', position, orientation)

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
        # Adjust the right boundary based on the last resistor's position
        right_boundary_x = max(comp[2][0] for comp in self.components if comp[0] == 'resistor')

        # Draw the square frame of the circuit
        square_coords = [
            (0, 0), (0, self.square_size),
            (right_boundary_x, self.square_size), (right_boundary_x, 0),
            (0, 0)
        ]
        self.ax.plot(*zip(*square_coords), 'k-')

        # Draw wires from the voltage source to the first resistor
        if len(self.components) > 1:
            v_source = self.components[0]
            first_resistor = self.components[0]

            # Draw wire from voltage source to the first series resistor
            self.ax.plot([v_source[2][0], first_resistor[2][0]], [v_source[2][1], first_resistor[2][1]], 'k-')

        # Connect all series resistors
        for i in range(1, len(self.components)):
            component = self.components[i]
            if component[0] == 'resistor' and component[3] == 'horizontal':
                if i > 1:  # If it's not the first resistor, connect it to the previous one
                    prev_component = self.components[i - 1]
                    self.ax.plot([prev_component[2][0], component[2][0]], [prev_component[2][1], component[2][1]], 'k-')

        # Connect parallel resistors
        for i in range(1, len(self.components)):
            component = self.components[i]
            if component[0] == 'resistor' and component[3] == 'vertical':
                # Connect to the top and bottom of the square
                self.ax.plot([component[2][0], component[2][0]], [self.square_size, component[2][1]], 'k-')  # Top wire
                self.ax.plot([component[2][0], component[2][0]], [0, component[2][1]], 'k-')  # Bottom wire


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
