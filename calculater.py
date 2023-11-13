import tkinter as tk
from tkinter import ttk

def on_click(button_value):
    current = entry_var.get()
    entry_var.set(current + button_value)

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def clear():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Style configuration
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 14), padding=10)
style.configure('TEntry', font=('Helvetica', 16), padding=10)

# Entry widget to display the current input
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    ttk.Button(root, text=button, style='TButton',
               command=lambda b=button: on_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
ttk.Button(root, text="C", style='TButton', command=clear).grid(row=row_val, column=col_val, sticky="nsew")

# Configure row and column weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
