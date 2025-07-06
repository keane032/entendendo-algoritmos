# caderno
caderno = dict()

caderno["maca"] = 0.67
caderno["leite"] = 1.40
caderno["abacate"] = 1.49

print(caderno)

print(caderno["abacate"])


# agenda

agenda = dict()

agenda["filipe"] = '9999-9999'
agenda["rodrigo"] = '9999-9999'

print(agenda["rodrigo"])

# urna

votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande Embora")
    else:
        votaram[nome] = True
        print("Deixe votar")

verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")