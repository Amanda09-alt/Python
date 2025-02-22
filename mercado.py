import tkinter as tk
from tkinter import messagebox 

# Função para adicionar item à lista
def adicionar_item():
    item = entry_item.get().strip()  # Obtém o item digitado e remove espaços extras
    if item:  # Verifica se o item não está vazio
        lista_compras.append(item)  # Adiciona o item à lista
        listabox_itens.insert(tk.END, item)  # Adiciona o item à ListBox
        entry_item.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        messagebox.showwarning("Aviso", "Digite um item para adicionar.")  # Aviso se o campo estiver vazio

# Função para remover item selecionado da lista
def remover_item():
    try:
        indice = listabox_itens.curselection()[0]  # Obtém o índice do item selecionado
        lista_compras.pop(indice)  # Remove o item da lista
        listabox_itens.delete(indice)  # Remove o item da ListBox
    except IndexError:
        messagebox.showerror("Aviso", "Selecione um item para remover.")  # Aviso se não estiver selecionado o item

# Função para mostrar os itens da lista em uma mensagem
def mostrar_itens():
    if lista_compras:
        itens = "\n".join(lista_compras)  # Junta os itens da lista em uma string com quebras de linha
        messagebox.showinfo("Lista de Compras", itens)  # Exibe os itens em uma caixa de mensagem
    else:
        messagebox.showinfo("Lista de Compras", "A lista está vazia.")  # Caso a lista esteja vazia

# Configuração da janela principal
janela = tk.Tk()
janela.title("Lista de Compras")
janela.geometry("300x300")

# Lista para armazenar os itens
lista_compras = []

# Campo de entrada para adicionar item
label_item = tk.Label(janela, text="Digite o item:")
label_item.pack(pady=5)

entry_item = tk.Entry(janela, width=30)
entry_item.pack(pady=5)

# Botão para adicionar item
botao_adicionar = tk.Button(janela, text="Adicionar Item", command=adicionar_item)
botao_adicionar.pack(pady=5)

# Listbox para exibir os itens
listabox_itens = tk.Listbox(janela, width=30)
listabox_itens.pack(pady=10)

# Botão para remover item
botao_remover = tk.Button(janela, text="Remover Item Selecionado", command=remover_item)
botao_remover.pack(pady=5)

# Botão para mostrar os itens
botao_mostrar = tk.Button(janela, text="Mostrar Lista", command=mostrar_itens)
botao_mostrar.pack(pady=5)

# Iniciar a interface gráfica
janela.mainloop()
