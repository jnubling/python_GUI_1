# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 15:45:51 2022

@author: jonna
"""

import tkinter as tk
from tkinter import ttk

# import some Dpi better control on WindowsOS for higher resolution screens
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def greet():
    print(f"Hello {user_name.get() or 'World'}")
# the first thing for creating an app is to create the main window
root = tk.Tk() # creates the main window 
root.title("Greeter App")

root.columnconfigure(0, weight=1) # expands the columns in 1x

user_name = tk.StringVar()# creates a text variable for user input

entry_frame = ttk.Frame(root, padding=(20, 10, 20, 0)) # creates a frame which will contain the user entry field
entry_frame.pack(side="top", fill="y", expand=True)

name_label = ttk.Label(entry_frame, text = "Name: ")
name_label.grid(column=0, row=0, padx=(0, 10)) 
# padx=(left and right, top and bottom) mesure
# .pack() puts the element into the window
# this label is going to be placed inside the the main window

name_entry = ttk.Entry(entry_frame, width=15, textvariable=user_name)
name_entry.grid(column=1, row=0)
name_entry.focus() # give it focus so typing is available right after rinning the application
# creates a field for user input and saves the input into the text variable "user_name"

buttons_frame = ttk.Frame(root, padding=(20, 10)) # creates a frame which will contain the buttons
buttons_frame.pack(side="top", expand=True)

greet_button = ttk.Button(buttons_frame, text="GREET", command=greet)
greet_button.grid(column=0, row=0, sticky="ew")
# creates a button in the main window that executes greet() when clicked

quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.grid(column=1, row=0, sticky="ew")
# creates a button that quit the application when clicked

root.mainloop() # runs the main window (should always be in the end of the code)


