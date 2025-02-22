#Inicío do código
import tkinter as tk
from tkinter import messagebox 

#Função para adicionar item à lista
def adicionar_item():
    item = entry_item.get().strip() #Obtém o item digitado o remove espaços extras
    if item: #Verifica se o item não está vazio
        lista_compras.append(item) #Adicionar o item
        listabox_itens.insert(tk.END, item) #Adicionar o item à ListBox
        entry_item.delete(0, tk.END) #Limpa o campo de entrada
    else:
        messagebox.showwarning("Avixo", "Digite um item para adicionar.") #Mostra um aviso se o campo estiver vazio
        
#Função para remover item selecionado da lista
def remove_item():
    try:
        indice = listabox_itens.curselection()[0] #Obitém o índice do item selecionado
        lista_compras.pop(indice) #Remove o item da lista
        listabox_itens.delete(indice) #Remove o item da lista
    except IndexError:
        messagebox.showerror("Aviso", "Selecione um item para remover.") #Mostrar um aviso se não estive selecionado o item

#Configuração da janela principal
janela = tk.Tk()
janela.title("Lista de compra")
janela.geometry("300x300")

#Lista para armazenar os itens
lista_compras = []

#Campo de entrada para adicionar item
label_item = tk.Label(janela, text="Digita o item:")
label_item.pack(pady=5)

entry_item = tk.Entry(janela, width=30)
entry_item.pack(pady=5)

#Botão para adicionar item
botao_adicionar = tk.Button(janela, text="Adicionar Item", command=adicionar_item)
botao_adicionar.pack(pady=5)

#Listabox para exibir os itens
listabox_itens = tk.Listbox(janela, width=30)
listabox_itens.pack(pady=10)

#Botão para remover item
botao_remover = tk.Button(janela, text="Remover item Selecionado", command=remover_item)
botao_remover.pack(pady=5)

#Botão para mostrar o item
botao_mostrar = tk.Button(janela, text="Mostara Lista", command=mostrar_item)
botao_mostrar.pack(pady=5)

#Iniciar a interface gráfica
janela.mainloop()