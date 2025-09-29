import random

def embaralhaNomes(nomes):
    random.shuffle(nomes)
    return nomes

def escolheNomes(nomes):
    nome = random.choice(nomes)
    return nome
def removeNome(nomes,nome):
    nomes.remove(nome)
    return nomes
def sorteiaNomes(nomes,tipo = "Normal"):
    while(len(nomes )>1):
        Nembaralhados = embaralhaNomes(nomes)
        Nselecionado = escolheNomes(nomes)

        if tipo == "Normal":
            return Nselecionado
        else:
            nomes = removeNome(nomes,Nselecionado)
            print("Eliminado(a):",Nselecionado)
            return Nselecionado,nomes
    return nomes[0]