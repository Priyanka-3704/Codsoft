import tkinter as tk
from tkinter import ttk
import string
import random
import pyperclip

def generate_password():
    password_length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        result_label.config(text="Please select at least one character type.")
    else:
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        result_label.config(text=generated_password)

def copy_to_clipboard():
    generated_password = result_label.cget("text")
    pyperclip.copy(generated_password)
    result_label.config(text="Password copied to clipboard!")

# Create the tkinter application
root = tk.Tk()
root.title("Password Generator")

# Center the window on the screen
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set background color
root.configure(bg="#f0f0f0")  # Replace "#f0f0f0" with the desired background color

# Create widgets
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14))
style.configure('TButton', font=('Helvetica', 14))

length_label = ttk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = ttk.Entry(root)
length_entry.pack(pady=5)

lowercase_var = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack(anchor='w')

uppercase_var = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(anchor='w')

digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(anchor='w')

special_var = tk.BooleanVar()
special_check = ttk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack(anchor='w')

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

result_label = ttk.Label(root, text="", font=("Helvetica", 16, "bold"), wraplength=400, justify='center')
result_label.pack(pady=20)

root.mainloop()
