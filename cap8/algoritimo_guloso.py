#algoritimo guloso: A cada etapa escolhe a solucao ideal e ao final terar uma solucao global ideal.

estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estacoes = {}

estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()


while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao # veirifica a interseção entre os conjuntos 
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos # remove estados que ja foram adicionados
    estacoes_final.add(melhor_estacao)



print(estacoes_final)


# Algoritmo	             | É guloso?   | Justificativa
# Dijkstra	             |  ✅ Sim	  |Escolhe o vértice com menor distância estimada a cada passo. sem reconsiderar essa escolha depois
# Quick Sort             |	❌ Não	  |Usa dividir-para-conquistar, não faz escolhas "ótimas locais".
# Busca em Largura (BFS) |	❌ Não	  |Percorre níveis, sem critério de custo ou ganho imediato.