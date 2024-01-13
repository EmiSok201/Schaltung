import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from os.path import join, dirname, abspath
from PIL import Image

class DrawCircuit:

    @staticmethod
    def draw():

        script_dir = dirname(abspath(__file__))

        fig, ax = plt.subplots()
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 5)

        # Load images for components
        resistor_parallel_path = join(script_dir, 'Resistor_Parallel.png')
        resistor_series_path = join(script_dir, 'Resistor_Reihe.png')
        voltage_source_path = join(script_dir, 'Voltage_Source.png')

        # Place images on the diagram
        resistor1_image = Image.open(resistor_series_path)
        resistor1_imagebox = OffsetImage(resistor1_image, zoom=0.25)
        resistor1_ab = AnnotationBbox(resistor1_imagebox, (2.25, 3.25), frameon=False, pad=0.1)
        ax.add_artist(resistor1_ab)

        # Place images on the diagram
        resistor2_image = Image.open(resistor_parallel_path)
        resistor2_imagebox = OffsetImage(resistor2_image, zoom=0.25)
        resistor2_ab = AnnotationBbox(resistor2_imagebox, (3.5, 2.25), frameon=False, pad=0.1)
        ax.add_artist(resistor2_ab)

        resistor3_image = Image.open(resistor_parallel_path)
        resistor3_imagebox = OffsetImage(resistor3_image, zoom=0.25)
        resistor3_ab = AnnotationBbox(resistor3_imagebox, (4.5, 2.25), frameon=False, pad=0.1)
        ax.add_artist(resistor3_ab)

        voltage_source_image = Image.open(voltage_source_path)
        voltage_source_imagebox = OffsetImage(voltage_source_image, zoom=0.25)
        voltage_source_ab = AnnotationBbox(voltage_source_imagebox, (1.25, 2.25), frameon=False, pad=0.1)
        ax.add_artist(voltage_source_ab)

        # Connect components with lines
        lines = [(1.25, 2.25), (1.25, 3.25), (3.5, 3.25), (3.5, 1.5), (1.25, 1.5), (1.25, 2.25)]
        for i in range(len(lines) - 1):
            ax.plot([lines[i][0], lines[i + 1][0]], [lines[i][1], lines[i + 1][1]], color='black')

        lines2 = [(3.5, 3.25), (4.5, 3.25), (4.5, 1.5), (3.5, 1.5)]
        for i in range(len(lines2) - 1):
            ax.plot([lines2[i][0], lines2[i + 1][0]], [lines2[i][1], lines2[i + 1][1]], color='black')

        ax.set_aspect('equal', adjustable='datalim')
        ax.axis('off')

        plt.show()
