# pesquisa em largura em um grafo
# fiz umas mundacas em relacao ao codigo origina mas e quase a msm coisa

from collections import deque

grafo = {}

grafo["voce"] = [
    {"name":"alice", "seller": False}, 
    {"name":"bob", "seller": False}, 
    {"name":"clarie", "seller": False}
]
grafo["alice"] = [
    {"name": "peggy", "seller": True}
]
grafo["bob"] = [
    {"name": "peggy", "seller": True},
    {"name": "anuj", "seller": False}
]
grafo["clarie"] = [
    {"name": "thom", "seller": False},
    {"name": "jonny", "seller": False}
]

grafo["peggy"] = []
grafo["anuj"] = []
grafo["thom"] = []
grafo["jonny"] = []

fila_de_pesquisa = deque() # cria um a lista nova
fila_de_pesquisa = grafo["voce"] # adicona seus vizinhos a lista 

verificados = []

while fila_de_pesquisa: # enquanto a lista estiver vazia
    pessoa = fila_de_pesquisa.pop() #pega primeiro da fila
    if not pessoa in verificados:
        if pessoa["seller"]: # verifica se a pessoa e um vendedor
            print(pessoa)
            break
        else:
            fila_de_pesquisa += grafo[pessoa["name"]] # adiciona seus vizinhos/filhos dessa pessoa a lista
            verificados.append(pessoa)

