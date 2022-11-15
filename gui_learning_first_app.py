# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 15:45:51 2022

@author: jonna
"""

import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello World")
# the first thing for creating an app is to create the main window
root = tk.Tk() # creates the main window 

ttk.Label(root, text = "Hello World", padding=(30, 10)).pack() 
# padding=(left and right, top and bottom) mesure
# .pack() puts the element into the window
# this label is going to be placed inside the the main window

greet_button = ttk.Button(root, text="GREET", command=greet)
greet_button.pack(side="left", fill="x", expand=True)
# creates a button in the main window that executes greet() when clicked

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="y", expand=True)
# creates a button that quit the application when clicked

root.mainloop() # runs the main window (should always be in the end of the code)


