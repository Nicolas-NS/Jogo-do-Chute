#teste
from tkinter import *
from jogo_chute1 import jogar

janela= Tk()
janela.title("Jogo do Chute")
janela.geometry('392x292')
janela.config(bg="#1e1e2e")

titulo = Label(janela, text='JOGO DO CHUTE', )
titulo.grid(column=0, row=0)

entrada = Entry(janela, ).grid(column=0, row=1)
janela.mainloop()