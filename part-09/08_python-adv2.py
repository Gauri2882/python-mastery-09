""" Project: Currency Converter """

import json
import tkinter as tk
from tkinter import ttk

def load_exchange_rates(file_path = "part-09/exchange_rates.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Exchange rate file not found!")
        return {}
    
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

def handle_conversion():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_dropdown.get()
        to_currency =  to_currency_dropdown.get()
        rates = load_exchange_rates()
        result = convert_currency(amount, from_currency, to_currency, rates)
        if result is not None:
            result_label.config(text = f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            result_label.config(text = "Conversion error!")
    except ValueError:
        result_label.config(text = "Invalid Amount!")

# main window 
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# amount entry
amount_label = tk.Label(root, text = "Amount:")
amount_label.pack(pady = 10)

amount_entry = tk.Entry(root)
amount_entry.pack(pady = 5)

# from currency dropdown
from_currency_label = tk.Label(root, text = "From currency: ")
from_currency_label.pack(pady = 5)

from_currency_dropdown = ttk.Combobox(root, values = ["USD", "EUR", "GBP", "INR", "JPY"])
from_currency_dropdown.pack(pady = 5)

# to currency dropdown
to_currency_label = tk.Label(root, text = "To currency: ")
to_currency_label.pack(pady = 5)

to_currency_dropdown = ttk.Combobox(root, values = ["USD", "EUR", "GBP", "INR", "JPY"])
to_currency_dropdown.pack(pady = 5)

# convert button
convert_button = tk.Button(root, text = "convert", command = handle_conversion)
convert_button.pack(pady = 10)

# result label
result_label = tk.Label(root, text= "", font = ("Arial", 14))
result_label.pack(pady = 10)

rates = load_exchange_rates()
amount = 100
converted = convert_currency(amount, "USD", "EUR", rates)
print(f"Converted {amount} USD to EUR: {converted:.2f}")

root.mainloop()