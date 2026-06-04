import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()

    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if numbers_var.get():
        characters += string.digits

    if special_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first!")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("650x450")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# Password Length
length_frame = tk.Frame(root)
length_frame.pack(pady=5)

tk.Label(
    length_frame,
    text="Password Length:",
    font=("Arial", 12)
).pack(side=tk.LEFT)

length_var = tk.IntVar(value=12)

length_spinbox = tk.Spinbox(
    length_frame,
    from_=4,
    to=50,
    textvariable=length_var,
    width=5
)
length_spinbox.pack(side=tk.LEFT, padx=10)

# Checkboxes
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Include Uppercase Letters",
    variable=uppercase_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Include Lowercase Letters",
    variable=lowercase_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=numbers_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Include Special Characters",
    variable=special_var
).pack(anchor="w", padx=50)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    width=20
)
generate_btn.pack(pady=15)

# Password Display
password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30,
    justify="center"
)
password_entry.pack(pady=10)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 12),
    width=20
)
copy_btn.pack(pady=10)

root.mainloop()