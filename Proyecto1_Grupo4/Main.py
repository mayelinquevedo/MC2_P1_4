import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

def agregar_vertice():
    vertice = entry_vertice.get()
    if vertice:
        lista_vertices.insert(tk.END, vertice)
        entry_vertice.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un vértice válido")

def agregar_arista():
    arista = entry_arista.get()
    if arista:
        lista_aristas.insert(tk.END, arista)
        entry_arista.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese una arista válida")

def generar_grafo():
    G = nx.DiGraph()  # Grafo dirigido
    # Agregar vértices
    for v in lista_vertices.get(0, tk.END):
        G.add_node(v)
    # Agregar aristas
    for a in lista_aristas.get(0, tk.END):
        u, v = a.split('->')
        G.add_edge(u.strip(), v.strip())
    
    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, font_size=10, font_weight='bold')
    plt.show()

root = tk.Tk()
root.title("Algoritmo de Grafos")

# Interfaz de ingreso de vértices y aristas
tk.Label(root, text="Vértice").grid(row=0, column=0)
entry_vertice = tk.Entry(root)
entry_vertice.grid(row=0, column=1)
tk.Button(root, text="Agregar Vértice", command=agregar_vertice).grid(row=0, column=2)

tk.Label(root, text="Arista (A -> B)").grid(row=1, column=0)
entry_arista = tk.Entry(root)
entry_arista.grid(row=1, column=1)
tk.Button(root, text="Agregar Arista", command=agregar_arista).grid(row=1, column=2)

# Lista de vértices y aristas
lista_vertices = tk.Listbox(root)
lista_vertices.grid(row=2, column=0, columnspan=3)
lista_aristas = tk.Listbox(root)
lista_aristas.grid(row=3, column=0, columnspan=3)

# Botón para generar el grafo
tk.Button(root, text="Generar Grafo", command=generar_grafo).grid(row=4, column=0, columnspan=3)




root.mainloop()


