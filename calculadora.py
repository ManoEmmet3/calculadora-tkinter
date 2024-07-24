from tkinter import *
from tkinter import ttk

cor_um = "#000000"    # preto
cor_dois = "#feffff"  # branco
cor_tres = "#38576b"  # azul
cor_quatro = "#ECEFF1" # cinza
cor_cinco = "#FFAB40" # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor_um)

tela = Frame(janela, width=235, height=50, bg=cor_tres)
tela.grid(row=0, column=0)

corpo_tela = Frame(janela, width=235, height=268)
corpo_tela.grid(row=1, column=0)

# Colocando botões

# linha 1

botao_um = Button(corpo_tela, text="Limpar", width=15, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_um.place(x=0, y=0)

botao_dois = Button(corpo_tela, text="%", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_dois.place(x=118, y=0)

botao_tres = Button(corpo_tela, text="/", width=5, height=2, bg=cor_cinco, fg=cor_dois, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_tres.place(x=177, y=0)

# linha 2
botao_quatro = Button(corpo_tela, text="7", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_quatro.place(x=0, y=46)

botao_cinco = Button(corpo_tela, text="8", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_cinco.place(x=59, y=46)

botao_seis = Button(corpo_tela, text="9", width=5, height=2, bg=cor_quatro, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_seis.place(x=118, y=46)

botao_sete = Button(corpo_tela, text="*", width=5, height=2, bg=cor_cinco, fg=cor_dois, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_sete.place(x=177, y=46)


# linha 3


# linha 4

janela.mainloop()

