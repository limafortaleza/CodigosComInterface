from tkinter import *
from tkinter import messagebox
from tkinter import ttk # importar o combobox

#storage in memory ==> simulação de banco de dados
agenda=[]
index=0


janela = Tk()
janela.title("Agenda Telefônica")   #função title--> que da títurlo pra janela
# janela.geometry('500x400')


def adicionarContato()-> None:
    nome=txt_nome.get()
    telefone=txt_telefone.get()
    categoria=cb_categorias.get()

    contato={
        'nome':nome,
        'telefone':telefone,
        'categoria':categoria
    }
    tabela.insert('',)
    agenda.append(contato)
    # print(agenda)
    limparCampos()
    atualizarTabela()
    messagebox.showinfo('Ok!', f'{nome} adicionado com sucesso!')

def editarContato()-> None:
    agenda[index]= {'Nome': txt_nome.get(),
                    'Telefone': txt_telefone.get(),
                    'Categoria': cb_categorias.get()}
    messagebox.showinfo('editado!', 'dados alterados com sucesso!')
    atualizarTabela()
    limparCampos()

def deletarContato() -> None:
    agenda.remove(agenda[index])
    messagebox.showinfo('deletado', 'Contato apagado com sucesso!')
    limparCampos()
    atualizarTabela()

def limparCampos() -> None:
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categorias.set('')  # set é como se atribuisse um valor para o combobox

def atualizarTabela() -> None: #atualizar os contatos na agenda,
    #limpando a tabela
    for linha in tabela.get_children(): #traz todas as linhas da tabela
        tabela.delete(linha)
    for contato in agenda:
        tabela.insert("", END, values=(contato['nome'], #essa aspas seria para representar o pai, como não há uma outra tabela
                                       contato['telefone'],
                                       contato['categoria']))

def tabelaClique(event) -> None:
    #pegando o indice da linha a partir da tupla criada, A tupla so tem 1 incide 0, por isso que passou [0]
    linha_selecionada =tabela.selection()
    global index
    index=tabela.index(linha_selecionada[0])
    contato=agenda[index]
    limparCampos()
    txt_nome.insert(0,contato['nome'])
    txt_telefone.insert(0, contato['telefone'])
    cb_categorias.set(contato['categoria'])


label_nome=Label(janela, text='Nome:', fg='red', font='Tahoma 14 bold')
label_nome.grid(row=0, column=0)


label_telefone=Label(janela, text='Telefone:', fg='red', font='Tahoma 14 bold')
label_telefone.grid(row=1, column=0)

#entry
txt_nome=Entry(janela, font='Tahoma 14',width=27)
txt_nome.grid(row=0,column=1)

txt_telefone=Entry(janela, font='Tahoma 14',width=27)
txt_telefone.grid(row=1,column=1)


#combobox (dropdownlist)

label_categorias=Label(janela, text='Categoria:', fg='red', font='Tahoma 14 bold')
label_categorias.grid(row=2, column=0)

categorias= ['Amigos', 'Familia', 'Trabalho'] #representar todos os itens do combobox
cb_categorias=ttk.Combobox(janela, values=categorias, width=25, font='Tahoma 14')
cb_categorias.grid(row=2, column=1)

#botao:
btn_adicionar=Button(janela, text='Adicionar', fg='red', font='Tahoma 12 bold', width=8,command=adicionarContato)
btn_adicionar.grid(row=3, column=0)


btn_editar=Button(janela, text='Editar', fg='red', font='Tahoma 12 bold', width=8,command=editarContato)
btn_editar.grid(row=3, column=1)

btn_deletar=Button(janela, text='Deletar', fg='red', font='Tahoma 12 bold', width=8,command=deletarContato)
btn_deletar.grid(row=3, column=2)


colunas=['Nome', 'Telefone', 'Categoria'] #defdinindo as colunas da tabela, mas noa o nome delas

#Criando a tabela:
tabela=ttk.Treeview(janela, columns=colunas, show='headings' ) #se nao colocar o headings ele vai criar uma coluna antes, uma a mais. NO caso quano a gente coloca ele vai cirar somentes colunas com  os nomes ditos na lista.
tabela.heading('Nome', text='Nome')#nomeando os cabeçalhos da coluna.
tabela.heading('Telefone', text='Telefone')
tabela.heading('Categoria', text='Categoria')
tabela.grid(row=4,columnspan=3)#columnspan --> espacço de quantas colunas ela pode ocupar.

tabela.bind("<ButtonRelease-1>", tabelaClique) #criando um evento para a tabela. O primeiro é a ção e segundo é a função

#alternativa para a repetição da nomeação dos cabeçalhos das colunas feitas acima:
# for c in colunas:
#     tabela.heading(c, text=c)

janela.mainloop()       #função que executa a janela (coloca  a janela no ar)