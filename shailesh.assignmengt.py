import tkinter as tk
from tkinter import messagebox

# Sample dictionary
my_dict = {0: 10, 1: 20}

def add_key_value():
    try:
        # Get the input from the entry fields
        key = int(key_entry.get())
        value = int(value_entry.get())

        # Add the new key-value pair to the dictionary
        my_dict[key] = value

        # Update the label to display the updated dictionary
        dict_label.config(text=f"Updated Dictionary: {my_dict}")

        # Show success message
        messagebox.showinfo("Success", f"Key {key} with value {value} added.")
    except ValueError:
        # Handle invalid input
        messagebox.showerror("Invalid Input", "Please enter valid integers for both key and value.")

# Set up the main tkinter window
root = tk.Tk()
root.title("Add Key to Dictionary")
root.geometry("600x400")

# Create and place the labels, entry fields, and button
key_label = tk.Label(root, text="Enter Key:")
key_label.pack(pady=5)

key_entry = tk.Entry(root)
key_entry.pack(pady=5)

value_label = tk.Label(root, text="Enter Value:")
value_label.pack(pady=5)

value_entry = tk.Entry(root)
value_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Key-Value", command=add_key_value)
add_button.pack(pady=10)

dict_label = tk.Label(root, text=f"Current Dictionary: {my_dict}")
dict_label.pack(pady=10)

# Start the tkinter main loop
root.mainloop()