from tkinter import *
from tkinter import ttk

cor_um = "#000000"    # preto
cor_dois = "#feffff"  # branco
cor_tres = "#38576b"  # azul
cor_quatro = "#ECEFF1" # cinza
cor_cinco = "#FFAB40" # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x282")
janela.config(bg=cor_um)

tela = Frame(janela, width=235, height=50, bg=cor_tres)
tela.grid(row=0, column=0)

corpo_tela = Frame(janela, width=235, height=268)
corpo_tela.grid(row=1, column=0)


# criando label

app_label = Label(corpo_tela, text="123456789", width=16 , height=2)
app_label.place(x= 0, y= 0)

# Colocando botões

# linha 1
botao_1 = Button(corpo_tela, text="Clear", width=15, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=0)

botao_2 = Button(corpo_tela, text="%", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=118, y=0)

botao_3 = Button(corpo_tela, text="/", width=5, height=2, bg=cor_cinco, fg=cor_dois, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=177, y=0)

# linha 2
botao_4 = Button(corpo_tela, text="7", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=0, y=46)

botao_5 = Button(corpo_tela, text="8", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=59, y=46)

botao_6 = Button(corpo_tela, text="9", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=118, y=46)

botao_7 = Button(corpo_tela, text="*", width=5, height=2, bg=cor_cinco, fg=cor_dois, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=177, y=46)

# linha 3
botao_8 = Button(corpo_tela, text="4", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=0, y=92)

botao_9 = Button(corpo_tela, text="5", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=59, y=92)

botao_10 = Button(corpo_tela, text="6", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_10.place(x=118, y=92)

botao_11 = Button(corpo_tela, text="-", width=5, height=2, bg=cor_cinco, fg=cor_dois, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_11.place(x=177, y=92)

# linha 4
botao_12 = Button(corpo_tela, text="1", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_12.place(x=0, y=138)

botao_13 = Button(corpo_tela, text="2", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_13.place(x=59, y=138)

botao_14 = Button(corpo_tela, text="3", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_14.place(x=118, y=138)

botao_15 = Button(corpo_tela, text="+", width=5, height=2, bg=cor_cinco, fg=cor_dois, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_15.place(x=177, y=138)

# linha 5

botao_16 = Button(corpo_tela, text="0", width=15, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_16.place(x=0, y=183)

botao_17 = Button(corpo_tela, text=".", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_17.place(x=118, y=183)

botao_18 = Button(corpo_tela, text="=", width=5, height=2, bg=cor_cinco, fg=cor_dois, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_18.place(x=177, y=183)


janela.mainloop()
