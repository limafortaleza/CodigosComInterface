import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk # importar o combobox



janela = Tk()
janela.title("Agenda Telefônica")
janela.geometry('600x700')
janela.configure(background='grey',relief='sunken')

frame1=Frame(janela)
frame1.pack()

agenda=[]
index=0
def adicionar_contato()->None:
    contato=box_contato.get()
    telefone=box_telefone.get()
    categoria=combo_categoria.get()

    contato={
        'nome': contato,
        'telefone':telefone,
        'categoria': categoria
    }
    agenda.append(contato)
    limparCampos()

    tabela.insert('',END,values=(contato['nome'], #essa aspas seria para representar o pai, como não há uma outra tabela
                                       contato['telefone'],
                                       contato['categoria']))



def tabelaClique(event)->None:
    linha_selecionada =tabela.selection()
    global index
    tabela.insert('',END,)


    # print(linha_selecionada)


def editar()->None:
    pass



def apagar()->None:
    pass


def limparCampos() ->None:
    box_contato.delete(0,END)
    box_telefone.delete(0,END)
    combo_categoria.set('')





label_titulo=Label(frame1, text='AGENDA TELEFÔNICA', font='Arial 14 bold',justify='center', cursor='hand2',pady=20,fg='black',width=600)
label_titulo.pack()

label_contato=Label(janela, text='CONTATO:', font= 'Arial 14',fg='black', bg='white', width=15)
label_contato.place(x=0,y=100)
box_contato=Entry(janela, font='Arial 14',border=2, width=25)
box_contato.place(x=200, y=100)


label_telefone=Label(janela, text='TELEFONE:', font= 'Arial 14',fg='black', bg='white', width=15)
label_telefone.place(x=0,y=150)
box_telefone=Entry(janela, font='Arial 14',border=2, width=25)
box_telefone.place(x=200, y=150)

#combobox
label_categoria=Label(janela, text='CATEGORIA', font='Arial 14', fg='black', bg='white', width=15)
label_categoria.place(x=0,y=200)
categoria=['Amigos', 'Família', 'Trabalho','Crush']
combo_categoria=ttk.Combobox(janela, values=categoria, font='Arial 14',background='yellow', width=24)
combo_categoria.place(x=200, y=200)

#botões:
button_adicionar=Button(janela,text='Adicionar', font='Arial 14 bold',border=2, fg='red',bg='yellow', width=10,command=adicionar_contato)
button_adicionar.place(x=40,y=300)

button_editar=Button(janela,text='Editar', font='Arial 14 bold',border=2, fg='red',bg='yellow',width=10)
button_editar.place(x=200,y=300)

button_apagar=Button(janela,text='Apagar', font='Arial 14 bold',border=2, fg='red',bg='yellow',width=10)
button_apagar.place(x=360,y=300)

colunas=['Nome', 'Telefone', 'Categoria'] #defdinindo as colunas da tabela, mas noa o nome delas
tabela=ttk.Treeview(janela, columns=colunas, show='headings' ) #se nao colocar o headings ele vai criar uma coluna antes, uma a mais. NO caso quano a gente coloca ele vai cirar somentes colunas com  os nomes ditos na lista.
tabela.heading('Nome', text='Nome')
tabela.heading('Telefone', text='Telefone')
tabela.heading('Categoria', text='Categoria')
tabela.column('Nome',minwidth=0,width=200)
tabela.column('Telefone',minwidth=0,width=120)
tabela.column('Categoria',minwidth=0,width=130)
tabela.place(x=40,y=400)
# for c in colunas:
#     tabela.heading(c, text=c, minwidth='50')
#     print(c)

tabela.bind("<ButtonRelease-1>", tabelaClique)


janela.mainloop()