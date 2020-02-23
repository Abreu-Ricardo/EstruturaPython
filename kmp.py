# Programador: Ricardo Abreu de Oliveira
def forcaBruta(t, p):
    tamt = len(t)
    tamp = len(p)

    l = tamt - tamp

    contador_de_iteracoes = 0
    cont = 0
    r = 0       # Numero de ocorrencias de p em t

    for i in range(l+1):
        for j in range(tamp):

            if t[i+j] == p[j]:
                cont = cont + 1
                contador_de_iteracoes = contador_de_iteracoes + 1
        
            else:
                i = i + j
                break
    
        if cont == tamp:    # Se cont == tamanho da palavra
            r = r + 1
        cont = 0
    print("Numero de comparacoes na forca bruta:",contador_de_iteracoes)
    return r




def calculaD (p, tamp, d):
    j = 0
    k = 1
    d[0] = 0

    while k < tamp:
        if p[k] == p[j]:        # Se for igual d[k] recebe j incrementado
            j = j + 1           # e anda para a proxima posicao do vetor
            d[k] = j
            k = k + 1

        else:
            if j == 0:          # Se forem diferentes e j == 0
                d[k] = 0        # quer dizer que nehum item do vetor
                k = k + 1       # ate agora eh igual a primeira posicao

            else:
                j = d[j-1]      # Se for diferente e j != 0
    return d                    # quer dizer que ja teve um item 
                                # igual ao primeiro, entao volta
                                # a partir da onde j esta



def kmp(t, p):

    tamt = len(t)
    tamp = len(p)

    d = [0]*tamp
    vetord = calculaD(p, tamp, d)

    i = 0
    j = 0
    r = 0       # Numero de ocorrencias de p em t

    contador_de_iteracoes = 0

    while i < tamt:

        if j == tamp:
            j = vetord[j-1]

        if t[i] == p[j]:
            j = j + 1   
            i = i + 1
            contador_de_iteracoes = contador_de_iteracoes + 1

            if j == tamp:
                r = r + 1
                j = 0

        elif i < tamt:
            if j != 0:
                j = vetord[j-1]
            else:
                i = i + 1
    print("Numero de comparacoes no kmp:",contador_de_iteracoes)

    return r





# main
t = input()
p = input()
tamp = len(p)
d = [0]*tamp
r = calculaD(p, tamp, d)
print(r)
#resposta = kmp(t, p)
#print("Numero de vezes de ocorrencia de p em q:",resposta)

#print()

#resposta = forcaBruta(t, p)
#print("Numero de vezes de ocorrencia de p em q:",resposta)
