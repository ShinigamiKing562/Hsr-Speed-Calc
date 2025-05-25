import tkinter as tk
from tkinter import font

def speed_required():
    try:
        turns = int(ent_turns.get()) * 10000
        cycles = 150 + (int(ent_cycles.get()) * 100)
        ddd = int(ent_ddd.get()) * 2400
        eagle = int(ent_eagle.get()) * 2500
        speed = (turns - ddd - eagle) / cycles
        lbl_speed["text"] = f"Speed: {round(speed, 2)}"
    except ValueError:
        lbl_speed["text"] = "Please enter valid numbers."

# Setup Window
window = tk.Tk()
window.title('Boothill')
window.geometry("350x300")
window.resizable(False, False)

# Fonts
label_font = font.Font(family="Helvetica", size=10)
entry_font = font.Font(family="Helvetica", size=10)
button_font = font.Font(family="Helvetica", size=10, weight="bold")

# Main Frame
frm_entry = tk.Frame(master=window, padx=20, pady=20)
frm_entry.pack()

# Labels and Entries
fields = [
    ("Number of turns", "ent_turns"),
    ("Number of cycles", "ent_cycles"),
    ("Number of DDD procs", "ent_ddd"),
    ("Number of eagle procs", "ent_eagle")
]

entries = {}

for i, (label_text, var_name) in enumerate(fields):
    lbl = tk.Label(master=frm_entry, text=label_text, font=label_font)
    lbl.grid(row=i, column=0, sticky="e", pady=5)
    ent = tk.Entry(master=frm_entry, font=entry_font)
    ent.grid(row=i, column=1, pady=5, padx=(10, 0))
    entries[var_name] = ent

# Reference entry widgets
ent_turns = entries["ent_turns"]
ent_cycles = entries["ent_cycles"]
ent_ddd = entries["ent_ddd"]
ent_eagle = entries["ent_eagle"]

# Button
btn_speed = tk.Button(
    master=window,
    text="Calculate",
    command=speed_required,
    font=button_font,
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
btn_speed.pack(pady=(10, 5))

# Result Label
lbl_speed = tk.Label(master=window, text="", font=("Helvetica", 12, "bold"))
lbl_speed.pack()

# Run App
window.mainloop()
