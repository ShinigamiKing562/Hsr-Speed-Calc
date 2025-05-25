import tkinter as tk
from tkinter import font
import os

class Boothill:
    def __init__(self, root):
        self.root = root
        self.root.title('Boothill')
        self.root.geometry("350x300")
        self.root.resizable(False, False)

        # Load icon safely
        try:
            icon_path = os.path.join(os.getcwd(), 'Icon', 'Boothill.ico')
            self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Warning: Icon not loaded. Reason: {e}")

        # Fonts
        self.label_font = font.Font(family="Helvetica", size=10)
        self.entry_font = font.Font(family="Helvetica", size=10)
        self.button_font = font.Font(family="Helvetica", size=10, weight="bold")

        # Entry fields dictionary
        self.entries = {}

        # Build UI
        self.build_interface()

    def build_interface(self):
        frm_entry = tk.Frame(self.root, padx=20, pady=20)
        frm_entry.pack()

        fields = [
            ("Number of turns", "ent_turns"),
            ("Number of cycles", "ent_cycles"),
            ("Number of DDD procs", "ent_ddd"),
            ("Number of eagle procs", "ent_eagle"),
            ("Base speed", "ent_base"),
            ("In-Battle speed boost", "ent_buff")
        ]

        for i, (label_text, var_name) in enumerate(fields):
            lbl = tk.Label(frm_entry, text=label_text, font=self.label_font)
            lbl.grid(row=i, column=0, sticky="e", pady=5)
            ent = tk.Entry(frm_entry, font=self.entry_font)
            ent.grid(row=i, column=1, pady=5, padx=(10, 0))
            self.entries[var_name] = ent

        self.lbl_speed = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"))
        self.lbl_speed.pack()

        btn_calc = tk.Button(
            self.root,
            text="Calculate",
            command=self.calculate_speed,
            font=self.button_font,
            bg="#D2401B",
            fg="white",
            padx=10,
            pady=5
        )
        btn_calc.pack(pady=(10, 5))

        btn_clear = tk.Button(
            self.root,
            text="Clear",
            command=self.clear_fields,
            font=self.button_font,
            bg="#555555",
            fg="white",
            padx=10,
            pady=5
        )
        btn_clear.pack(pady=(0, 10))

    def calculate_speed(self):
        try:
            turns = float(self.entries["ent_turns"].get()) * 10000
            cycles = 150 + (float(self.entries["ent_cycles"].get()) * 100)
            ddd = float(self.entries["ent_ddd"].get()) * 2400
            eagle = float(self.entries["ent_eagle"].get()) * 2500
            base = float(self.entries["ent_base"].get())
            buff = base * 0.01 * float(self.entries["ent_buff"].get())

            speed = (turns - ddd - eagle) / cycles - buff
            self.lbl_speed.config(text=f"Speed: {round(speed, 2)}", fg="black")
        except ValueError:
            self.lbl_speed.config(text="Please enter valid numbers.", fg="red")

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.lbl_speed.config(text="", fg="black")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = Boothill(root)
    root.mainloop()
