import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_backspace():
    current = entry.get()
    entry.delete(len(current) - 1)

def button_square_root():
    current = entry.get()
    try:
        result = eval(current) ** 0.5
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Beautiful Calculator")
window.configure(bg="lightgray")

# Set custom font
custom_font = Font(family="Helvetica", size=16)

# Create the entry widget with larger width and columnspan
entry = ttk.Entry(window, font=custom_font, width=30)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Create style for the buttons
style = ttk.Style()
style.configure("TButton", font=custom_font, padding=8)

# Create number buttons with attractive colors
button_1 = ttk.Button(window, text="1", command=lambda: button_click(1), style="TButton", width=5, takefocus=False)
button_2 = ttk.Button(window, text="2", command=lambda: button_click(2), style="TButton", width=5, takefocus=False)
button_3 = ttk.Button(window, text="3", command=lambda: button_click(3), style="TButton", width=5, takefocus=False)
button_4 = ttk.Button(window, text="4", command=lambda: button_click(4), style="TButton", width=5, takefocus=False)
button_5 = ttk.Button(window, text="5", command=lambda: button_click(5), style="TButton", width=5, takefocus=False)
button_6 = ttk.Button(window, text="6", command=lambda: button_click(6), style="TButton", width=5, takefocus=False)
button_7 = ttk.Button(window, text="7", command=lambda: button_click(7), style="TButton", width=5, takefocus=False)
button_8 = ttk.Button(window, text="8", command=lambda: button_click(8), style="TButton", width=5, takefocus=False)
button_9 = ttk.Button(window, text="9", command=lambda: button_click(9), style="TButton", width=5, takefocus=False)
button_0 = ttk.Button(window, text="0", command=lambda: button_click(0), style="TButton", width=5, takefocus=False)

# Create operator buttons with attractive colors
button_add = ttk.Button(window, text="+", command=lambda: button_click("+"), style="TButton", width=5, takefocus=False)
button_subtract = ttk.Button(window, text="-", command=lambda: button_click("-"), style="TButton", width=5, takefocus=False)
button_multiply = ttk.Button(window, text="*", command=lambda: button_click("*"), style="TButton", width=5, takefocus=False)
button_divide = ttk.Button(window, text="/", command=lambda: button_click("/"), style="TButton", width=5, takefocus=False)
button_equal = ttk.Button(window, text="=", command=button_equal, style="TButton", width=12, takefocus=False)
button_clear = ttk.Button(window, text="C", command=button_clear, style="TButton", width=5, takefocus=False)
button_backspace = ttk.Button(window, text="⌫", command=button_backspace, style="TButton", width=5, takefocus=False)  # Backspace symbol
button_square_root = ttk.Button(window, text="√", command=button_square_root, style="TButton", width=5, takefocus=False)
button_decimal = ttk.Button(window, text=".", command=lambda: button_click("."), style="TButton", width=5, takefocus=False)

# Position buttons on the grid with spacing
button_1.grid(row=1, column=0, padx=5, pady=5)
button_2.grid(row=1, column=1, padx=5, pady=5)
button_3.grid(row=1, column=2, padx=5, pady=5)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_7.grid(row=3, column=0, padx=5, pady=5)
button_8.grid(row=3, column=1, padx=5, pady=5)
button_9.grid(row=3, column=2, padx=5, pady=5)
button_0.grid(row=4, column=0, padx=5, pady=5)
button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)
button_equal.grid(row=5, column=2,columnspan=2, padx=5, pady=5)  # Changed the columnspan to 2
button_clear.grid(row=5, column=0, padx=5, pady=5)
button_backspace.grid(row=5, column=1, padx=5, pady=5)
button_square_root.grid(row=4, column=2, padx=5, pady=5)
button_decimal.grid(row=4, column=1, padx=5, pady=5)

# Run the main window loop
window.mainloop()
