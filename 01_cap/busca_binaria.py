def pesquisa_binaria(lista, item):
    baixo = 0 #baixo e alto acompanham a parte da lista que voce esta procurando
    alto = len(lista) - 1 #
    while baixo <= alto: # enquanto não conseguiu achar o elemento
        meio = (baixo + alto) / 2 # vericfica o elemento central
        chute = lista[meio]
        if chute == item: # acha o item 
            return meio
        if chute > item: # o chute foi muito alto
            alto = meio - 1
        else: # o chute foi muito baixo
            baixo = meio + 1
    return None # item nao existe



minhaLista = [1,3,5,7,9]

print(pesquisa_binaria(minhaLista,3))
print(pesquisa_binaria(minhaLista,-1))


