from tkinter import *
from tkinter import ttk

color_one = "#000000"    #  preto
color_two = "#feffff"    #  branco
color_three = "#38576b"  #  azul 
color_four = "ECEFF1"    #  cinza
color_five = "#FFAB40"   #  laranja

window = Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(bg=color_one)

screen = Frame(window , width=235, height=50 , bg=color_three)
screen.grid(row=0, column=0)

screen_body = Frame(window , width=235, height=268, )
screen_body.grid(row=1, column=0)

# Placing buttons

# row 1 

buttons_one = Button(screen_body, text="Clean", width=15, height=2)
buttons_one.place(x=0, y=0)

buttons_two = Button(screen_body, text="%", width=5, height=2)
buttons_two.place(x=120, y=0)

buttons_three = Button(screen_body, text="/", width=5, height=2)
buttons_three.place(x=180, y=0)
# row 2 

window.mainloop()