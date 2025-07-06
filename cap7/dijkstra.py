
#     Inicio
#     /   \
#    2     6
#   /       \
#  B →  3  → A
#   \        /
#    5      1
#     \    /
#      Fim

grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

print(grafo["inicio"].keys())

print(grafo["inicio"]["a"])
print(grafo["inicio"]["b"])

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}


print(grafo["a"])
print(grafo["b"])

infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito



pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

print(pais)

processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo =   float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


nodo = ache_no_custo_mais_baixo(custos) #encontra o custo mais baixo

while nodo is not None: # enquanto existir nos a ser processados executa o trecho abaixo
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys(): # percorre os vizinhos do vertice
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo: # caso seja mais barato chegar a um vizinho a partir desse vertice....
            custos[n] = novo_custo # ...atualiza custo
            pais[n] = nodo # esse vertice se torna o novo pai para o vizinho
    processados.append(nodo) # marca como processado 
    nodo = ache_no_custo_mais_baixo(custos) # passa para o proximo vertice e repe o algoritimo


print("===========")
print(pais)

