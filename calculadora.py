from tkinter import *
from tkinter import ttk

color = "#000000"

window = Tk()
window.title("Calculadora")
window.geometry("235x318")

screen = Frame(window , width=235, height=50 , bg=color)
screen.grid(row=0, column=0)


window.mainloop()