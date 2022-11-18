# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 13:22:27 2022

@author: jonna
"""

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Conversor de Distâncias")

metres_value = tk.StringVar()  # holds the typed value of metres
metres_converted = tk.StringVar(value="Feet shown here")  # holds the converted value of metres

def calculator(*args):
    
    try:
        metres_converted.set(float(metres_value.get()) * 3.28084)
    except ValueError:
        metres_converted.set("Value Error")


main_frame = ttk.Frame(
    root,
    padding=(50,10)
    )
main_frame.grid()

metres_label = ttk.Label(main_frame, 
                         text="Metres:",
                         font=(10)
                         )
metres_input = ttk.Entry(main_frame, 
                         width=10, 
                         textvariable=metres_value,
                         font=(10)
                         )
feet_label = ttk.Label(main_frame, 
                       text="Feet:",
                       font=(10)
                       )
feet_display = ttk.Label(main_frame, 
                         textvariable=metres_converted,
                         font=(10)
                         )
calc_button = ttk.Button(main_frame, 
                         text="Calculate",
                         command=calculator
                         )

metres_label.grid(column=0, row=0, sticky="w")
metres_input.grid(column=1, row=0, sticky="we")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="w")
feet_display.grid(column=1, row=1, sticky="we")

calc_button.grid(column=0, row=2, columnspan=2)

for child in main_frame.winfo_children():
    # ajusts every children in the main_frame 
    # to have the same padding in x and y
    child.grid_configure(padx=5, pady=5)
    
root.bind("<Return>", calculator)  
# allows calculation when the Enter Button in pressed

# root.bind("<KP_Enter>", calculator)





root.mainloop()