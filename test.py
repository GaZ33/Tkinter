from tkinter import *
from tkinter import ttk
root = Tk() # Criando a janela principal
root.title("Teste") # Dando um titulo a ela

mainframe = ttk.Frame(root, padding=50) # Criando um frame dentro da janela principal (root, ele é o pai)
mainframe.grid(row=0, column=0, sticky=(N, W , E, S)) # Dizendo qual será a grade do frame que criamos e como se comportará
mainframe.columnconfigure(0, weight=1) # Configurando as colunas do frame
mainframe.rowconfigure(0, weight=1) # Configurando as linhas do frame

root.mainloop()