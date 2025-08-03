" Project: Stock Market Dashboard "

import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# load the stock data
def load_data(file_path = "part-07/stock_data.csv"):
    return pd.read_csv(file_path)

data = load_data()

# initialize tkinter app

# create the main window
root = tk.Tk()
root.title("Stock Market Dashboard")
root.geometry("600x600")

# global variable for current canvas
current_canvas = None

# plot stock function 
def plot_stock_data(stock):
    global current_canvas
    if current_canvas:
        current_canvas.get_tk_widget().destroy()

    filtered_data = data[data['stock'] == stock]
    fig = Figure(figsize= (6, 4), dpi = 100)
    ax = fig.add_subplot(111)
    ax.plot(filtered_data['date'], filtered_data['price'], marker = "o", color = "green")
    ax.set_title(f"{stock} Stock Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    current_canvas = FigureCanvasTkAgg(fig, master = root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack()

# widgets

# dropdown for selecting stock
stock_label = tk.Label(root, text = "Select Stock:", font = ("Arial", 14))
stock_label.pack(pady = 5)

stock_dropdown = ttk.Combobox(root, values = ["AAPL", "MSFT"])
stock_dropdown.pack(pady = 5)

# button to plot data
plot_button = tk.Button(root, text = "Plot Stock Data", command = lambda: plot_stock_data(stock_dropdown.get()), font = ("Arial", 12))
plot_button.pack(pady = 10)

# run the application
root.mainloop()