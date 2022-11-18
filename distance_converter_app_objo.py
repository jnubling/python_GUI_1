# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:26:31 2022

@author: jonna
"""

import tkinter as tk
from tkinter import ttk


class ConversorDistancia(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Conversor de Distâncias")
        self.frames_dict = dict()
        
        container_frame = ttk.Frame(self) 
        container_frame.grid(padx=60, pady=30, sticky="wnes")
        # creates the main frame in the root window
        
        # metres_to_feet = MetresToFeet(container_frame, self)
        # metres_to_feet.grid(row=0, column=0, sticky="wnes")
        # # creates the metres-to-feet frame inside the main frame
        
        # feet_to_metres = FeetToMetres(container_frame, self)
        # feet_to_metres.grid(row=0, column=0, sticky="wnes")
        # # creates the feet-to-metres frame inside the main frame and
        # # in front of the metres-to-feet frame, one on top of the other
        
        # self.frames_dict[FeetToMetres] = feet_to_metres
        # self.frames_dict[MetresToFeet] = metres_to_feet
        # # creates a dictionary with keys and values for easy access later on
        
        # self.bind("<Return>", metres_to_feet.calculator)  
        # # allows calculation when the Enter Button in pressed

        # self.bind("<KP_Enter>", calculator)
        # if "enter" in num pad is not called with <Return>
        
        
        
        for FrameClass in (MetresToFeet, FeetToMetres):
            # creates all the frames and assign them to the frames dictionary
            frames = FrameClass(container_frame, self)
            self.frames_dict[FrameClass] = frames
            frames.grid(row=0, column=0, sticky="wnes")
            
        self.change_frame(MetresToFeet)    
        
    def change_frame(self, frame):
        # creates a function that changes the respective frame
        changing = self.frames_dict[frame]
        self.bind("<Return>", changing.calculator)
        changing.tkraise() # raises the respective frame to the front
        
        

class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
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
        switch_frame_button = ttk.Button(self,
                                         text="Feet -> Metres",
                                         command=lambda:
                                             controller.change_frame(
                                                 FeetToMetres
                                                 )
                                             )

        # -- Layout --

        metres_label.grid(column=0, row=0, sticky="we")
        metres_input.grid(column=1, row=0, sticky="we")
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky="we")
        feet_display.grid(column=1, row=1, sticky="we")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="we")
        switch_frame_button.grid(column=0, row=3, columnspan=2, sticky="we")
        

        for child in self.winfo_children():
           # ajusts every children in the main_frame 
           # to have the same padding in x and y
            child.grid_configure(padx=5, pady=5)
            
    def calculator(self, *args):
        
        try:
            self.metres_converted.set(float(self.metres_value.get()) * 3.28084)
        except ValueError:
            self.metres_converted.set("Value Error")
            
            
class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        
        self.feet_value = tk.StringVar()  # holds the typed value of metres
        self.feet_converted = tk.StringVar(value="Metres value shown here") 
        
        # -- Widgets --

        feet_label = ttk.Label(self, 
                                 text="Feet:",
                                 font=(10)
                                 )
        feet_input = ttk.Entry(self, 
                                 width=10, 
                                 textvariable=self.feet_value,
                                 font=(10)
                                 )
        metres_label = ttk.Label(self, 
                               text="Metres:",
                               font=(10)
                               )
        metres_display = ttk.Label(self, 
                                 textvariable=self.feet_converted,
                                 font=(10)
                                 )
        calc_button = ttk.Button(self, 
                                 text="Calculate",
                                 command=self.calculator
                                 )
        switch_frame_button = ttk.Button(self,
                                         text="Metres -> Feet",
                                         command=lambda:
                                             controller.change_frame(
                                                 MetresToFeet
                                                 )
                                             )

        # -- Layout --

        feet_label.grid(column=0, row=0, sticky="we")
        feet_input.grid(column=1, row=0, sticky="we")
        feet_input.focus()

        metres_label.grid(column=0, row=1, sticky="we")
        metres_display.grid(column=1, row=1, sticky="we")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="we")
        switch_frame_button.grid(column=0, row=3, columnspan=2, sticky="we")

        for child in self.winfo_children():
           # ajusts every children in the main_frame 
           # to have the same padding in x and y
            child.grid_configure(padx=5, pady=5)
            
    def calculator(self, *args):
        
        try:
            self.feet_converted.set(float(self.feet_value.get()) / 3.28084)
        except ValueError:
            self.feet_converted.set("Value Error")
            
            
        
root = ConversorDistancia()
root.columnconfigure(0, weight=1)

root.mainloop()