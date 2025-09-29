import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import sorteio
import database as db
from tkinter import filedialog
from tkinter.filedialog import askopenfile 
# import pdf

root = tk.Tk()
root.config(bg="lightgrey")
root.title("Sorteio")

label_Nome = tk.Label(root,text="Nome:")
label_Nome.config(bg="lightgrey")
label_Nome.grid(row=0,column=0,padx=5,pady=5)

entry_Nome = tk.Entry(root)
entry_Nome.grid(sticky=tk.EW,padx=5,pady=5,row=0,column=1)
entry_Nome.focus()

botao_inserir = tk.Button(root,text="Inserir",command=None)
botao_inserir.grid(column=2,row=0,padx=5,pady=5,ipadx=7,ipady=7)

botao_excluirTDS = tk.Button(root,text="Excluir Todos",command=None)
botao_excluirTDS.grid(column=3,row=0,padx=5,pady=5,ipadx=7,ipady=7)

frame_lista = tk.Frame(root)
frame_lista.grid(row=1)

listaDeNomes = tk.Listbox(root)
listaDeNomes.grid(row=1,columnspan=5,sticky=tk.EW)

#menu Butao direito
m = tk.Menu(root,tearoff=0)
m.add_command(label="Excluir",command=None)
m.add_separator()
m.add_command(label="Sair")

scrollbar = tk.Scrollbar(frame_lista,orient=tk.VERTICAL,command=listaDeNomes.yview)
listaDeNomes.configure(yscroll =scrollbar.set)
scrollbar.grid(row=1,column=1,sticky=tk.NS)

#escolher opções de sorteio
frame_radiusbutton = tk.Frame(root)
frame_radiusbutton.config(bg="lightgrey")
frame_radiusbutton.grid(row=2,columnspan=5)

valor_radiubutton = tk.StringVar()
valor_radiubutton.set('Normal')

radiubutton_sorteio_Normal = ttk.Radiobutton(frame_radiusbutton,text='Normal',variable=valor_radiubutton,value='Normal')
radiubutton_sorteio_Normal.grid(row=0,column=0,padx=10,pady=10)



radiubutton_sorteio_Ultimo = ttk.Radiobutton(frame_radiusbutton,text='Por eliminação',variable=valor_radiubutton,value='Ultimo')
radiubutton_sorteio_Ultimo.grid(row=0,column=1,padx=10,pady=10)

frame_Progressar = tk.Frame(root)
frame_Progressar.config(bg="lightgrey")
frame_Progressar.grid(row=3,columnspan=5)

barra_de_Progresso = ttk.Progressbar(frame_Progressar,orient=tk.HORIZONTAL,mode="determinate",length=350,value=0,maximum=100)
barra_de_Progresso.grid(row=0,column=0,columnspan=2)

label_barra_Progresso = tk.Label(frame_Progressar,text="Sorteando:%")
label_barra_Progresso.config(bg="lightgrey")
label_barra_Progresso.grid(row=0,column=0,columnspan=2)

frame_butoes = tk.Button(root)
frame_butoes.config(bg="lightgrey")
frame_butoes.grid(row=4,columnspan=5)

imagem_sortear = tk.PhotoImage(file="imgs/raffle.png")
imagem_sortear_menor = imagem_sortear.subsample(15,15)

butao_sortear = ttk.Button(frame_butoes,text="Sortear",image=imagem_sortear_menor,compound=tk.LEFT,command=None)

root.mainloop()


