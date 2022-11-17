# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:36:50 2022

@author: jonna
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400") # window opens in a default size
root.resizable(width=True, height=False)
root.title("Widget Examples")

# =============================================================================
# Label Widgets
# =============================================================================
# simple label
label = ttk.Label(root, text="Beethoven", padding=20)
label.config(font=(20))
label.grid(column=0, row=0)

# image
with open("logo.jpg", "rb") as f:
    image = Image.open(f).resize((64,125))
photo = ImageTk.PhotoImage(image)
label_image = ttk.Label(root, image=photo, padding=5)
label_image.grid(column=1, row=0)

# dinamic label
dinamicString = tk.StringVar()
label_dinamic = ttk.Label(root, textvariable=dinamicString, padding=10)
label_dinamic.config(font=15)
label_dinamic.grid(column=0, row=1)
dinamicString.set("This is a dinamic label")

# =============================================================================
# Text typing Widgets
# =============================================================================
text = tk.Text(root, height=10, width=30) 
text.grid(column=2, row=0, sticky="w")

text.insert("1.0", "This is a text widget...\nEnter your text here")
text["state"] = "normal" # or "disabled" if typing is no allowed
text_content = text.get("1.0", "end") 
# retrieves the text typed .get("starting", "ending")

# =============================================================================
# Scrollbar Widgets
# =============================================================================
text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
text_scroll.grid(column=2, row=0, sticky="ens")
text["yscrollcommand"] = text_scroll.set 

# =============================================================================
# Separator Widgets
# =============================================================================
ttk.Separator(root, orient="horizontal").grid(row=2, sticky="ew")

# =============================================================================
# Check Button Widgets
# =============================================================================
selected_option = tk.StringVar()
# stores the selected value when clicked(onvalue, offvalue)

def get_current_option():
    return selected_option.get()

check = ttk.Checkbutton(
    root,
    text="Check Button Example",
    variable=selected_option,
    textvariable=selected_option,
    command=get_current_option,
    onvalue="on",
    offvalue="off",
    state="normal"
    )

check.grid(column=0, row=3)

# =============================================================================
# Radio Button Widgets
# =============================================================================
storage_variable = tk.StringVar()
# stores the value of the selected option

def get_selected_option():
    print(storage_variable.get())
    return storage_variable.get()

option_one = ttk.Radiobutton(
    root,
    text=f"{'Option 1' or storage_variable.get()}",
    variable=storage_variable,
    command=get_selected_option,
    value="First Option Selected"
    )
option_two = ttk.Radiobutton(
    root,
    text="Option 2",
    variable=storage_variable,
    command=get_selected_option,
    value="Second Option Selected"
    )
option_three = ttk.Radiobutton(
    root,
    text="Option 3",
    variable=storage_variable,
    command=get_selected_option,
    value="Third Option Selected"
    )
option_one.grid(column=0)
option_two.grid(column=0)
option_three.grid(column=0)






























root.mainloop()