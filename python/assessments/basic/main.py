from tkinter import *
from tkinter import ttk
import csv

# Create a function that will update the balance.
def update_buttons():
    amount_buttons = amount.get()
    for i in range(amount_buttons):
        ttk.Button(root, text=f"Row 0, Col {i}").pack()

# Read csv items then return item
def read_csv(name_file):
    with open(f"{name_file}.csv", "r") as f:
        reader = csv.DictReader(f)
        items = list(reader)

    for item in items:
        return item

# GUI Code
root = Tk()
root.title("Goal Tracker")
root.geometry("500x200")

message_text = StringVar()
message_text.set("Enter what csv file to display below")

message_label = ttk.Label(root, textvariable=message_text, wraplength=250)
message_label.pack()

amount_label = ttk.Label(root, text="Amount of buttons:")
amount_label.pack()

amount = IntVar()
amount.set("")

amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.pack()

submit_button = ttk.Button(root, text="Submit", command=update_buttons)
submit_button.pack()

# Run mainloop
root.mainloop()




"""
Plans:
Make use of csv as storage, user will input something, stored into csv then have options
to delete, update, or create a csv.
"""