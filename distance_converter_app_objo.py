# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:26:31 2022

@author: jonna
"""

import tkinter as tk
from tkinter import ttk


class Conversor_distancia(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Conversor de Distâncias")
        
        main_frame = Main_Frame(self, padding=(50,10))
        main_frame.grid()
        
        self.bind("<Return>", main_frame.calculator)  
        # allows calculation when the Enter Button in pressed

        # self.bind("<KP_Enter>", calculator)
        # if "enter" in num pad is not called with <Return>
        

class Main_Frame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        
        self.metres_value = tk.StringVar()  # holds the typed value of metres
        self.metres_converted = tk.StringVar(value="Feet value shown here") 
        
        # -- Widgets --

        metres_label = ttk.Label(self, 
                                 text="Metres:",
                                 font=(10)
                                 )
        metres_input = ttk.Entry(self, 
                                 width=10, 
                                 textvariable=self.metres_value,
                                 font=(10)
                                 )
        feet_label = ttk.Label(self, 
                               text="Feet:",
                               font=(10)
                               )
        feet_display = ttk.Label(self, 
                                 textvariable=self.metres_converted,
                                 font=(10)
                                 )
        calc_button = ttk.Button(self, 
                                 text="Calculate",
                                 command=self.calculator
                                 )

        # -- Layout --

        metres_label.grid(column=0, row=0, sticky="w")
        metres_input.grid(column=1, row=0, sticky="we")
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky="w")
        feet_display.grid(column=1, row=1, sticky="we")

        calc_button.grid(column=0, row=2, columnspan=2)

        for child in self.winfo_children():
           # ajusts every children in the main_frame 
           # to have the same padding in x and y
            child.grid_configure(padx=5, pady=5)
            
    def calculator(self, *args):
        
        try:
            self.metres_converted.set(float(self.metres_value.get()) * 3.28084)
        except ValueError:
            self.metres_converted.set("Value Error")
            
            
        
root = Conversor_distancia()
root.columnconfigure(0, weight=1)

root.mainloop()