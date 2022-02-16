
from tkinter import *

'''Window'''
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

'''Miles'''
miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

'''km converter'''
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

'''Km'''
km_output = Label(text="0")
km_output.grid(column=1,row=1)
km_label = Label(text="Km")
km_label.grid(column=2,row=1)

'''Calculate'''
def calculate_button():
    miles = float(miles_input.get())
    km = 1.60934 * miles
    km_output["text"] = f"{km}"
calculate = Button(text="Calculate", command=calculate_button)
calculate.grid(column=1,row=2)

window.mainloop()
