# Programador: Ricardo Abreu de Oliveira

t = input()
p = input()

tamt = len(t)
tamp = len(p)

l = tamt - tamp

cont = 0
r = 0

for i in range(l+1):
    for j in range(tamp):

        if t[i+j] == p[j]:
            cont = cont + 1
        
        else:
            i = i + j
            break
    
    if cont == tamp:    # Se cont == tamanho da palavra
        r = r + 1
    cont = 0

print(r)