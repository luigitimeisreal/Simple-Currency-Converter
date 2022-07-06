import tkinter
from forex_python.converter import CurrencyRates


def calculate(source,destination):
    c = CurrencyRates()
    return c.get_rate(source, destination)


def convert():
    try:
        # Checks if it's a number
        initial = float(quantity.get())
        # Displays the amount of money
        rate = calculate(clicked.get(), clicked_dest.get())
        result = initial * rate
        label = tkinter.Label(window, text=f"{quantity.get()} {clicked.get()} is {result} {clicked_dest.get()}",
                              font=("Calibri", 12))
        label.pack(side=tkinter.BOTTOM)
    except:
        label = tkinter.Label(window, text="Not a valid number", font=("Calibri", 12))
        label.pack(side=tkinter.BOTTOM)


def get_quantity():
    print(quantity.get())
    return int(quantity.get())


def display_result(event):
    print(clicked.get())

currencies = ["EUR","USD", "IDR", "BGN", "GBP", "DKK", "CAD","JPY", "HUF", "RON", "MYR", "SEK", "SGD", "AUD","CHF"]


# Define the window
window = tkinter.Tk()
window.geometry("756x500")

# title
label = tkinter.Label(window,text="Currency Converter",font=("Calibri",20))
label.pack()

# User input
quantity = tkinter.Entry(window)
quantity.pack()

# Convert button
currency_convert = tkinter.Button(window, text="Convert", padx=20, command=convert)
currency_convert.pack()

# Select source currency
clicked = tkinter.StringVar()
clicked.set(currencies[0])
source = tkinter.OptionMenu(window,clicked,*currencies)
source.pack(side=tkinter.LEFT,padx=50)

# Select destination currency
clicked_dest = tkinter.StringVar()
clicked_dest.set(currencies[0])
destination = tkinter.OptionMenu(window,clicked_dest,*currencies)
destination.pack(side=tkinter.RIGHT,padx=50)

# Main loop (displays the program all the time)
window.mainloop()

