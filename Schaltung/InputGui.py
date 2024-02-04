import tkinter as tk
from tkinter import messagebox

class ResistorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Resistor Input GUI")
        self.setup_widgets()

    def setup_widgets(self):
        tk.Label(self.master, text="Resistor R1 (ohms):").grid(row=0)
        tk.Label(self.master, text="Resistor R2 (ohms):").grid(row=1)

        self.r1_entry = tk.Entry(self.master)
        self.r2_entry = tk.Entry(self.master)

        self.r1_entry.grid(row=0, column=1)
        self.r2_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, columnspan=2)

    def submit(self):
        try:
            r1_value = float(self.r1_entry.get())
            r2_value = float(self.r2_entry.get())
            messagebox.showinfo("Submitted Values", f"Resistor R1: {r1_value} ohms\nResistor R2: {r2_value} ohms")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")
