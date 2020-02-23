# Programador: Ricardo Abreu de Oliveira

class No:
    def __init__ (self, info, tam):
        self.info = info
        self.pai = self.dir = self.esq = None
        self.b = 0
        self.tam = tam # Campo para armazenar o tamanho de cada palavra

def erd(T):
    # Recursão para imprimir em ordem simétrica
    if T != None:
        if T.esq != None:
            erd(T.esq)

        # Método para imprimir na mesma linha com espaço entre as palavras,
        # porém fica com espaço na última palavra 
        print(T.info, '', end='')        
        
        if T.dir != None:
            erd(T.dir)

def insere_Arvore (T, x):
    
    if T == None and x != None:
        return x

    novo = No(x.info, x.tam)
        
    if T.tam < novo.tam:
        T.esq = insere_Arvore(T.esq, novo)

    else:
        T.dir = insere_Arvore(T.dir, novo)

    return  T   #retorna o novo nó na posição certa     
        


  

n = int(input())

for i in range(n):
    entrada = input().split()

    T = None

    for j in range(len(entrada)):

        x = No(entrada[j], len(entrada[j])) # Novo nó já vai com o seu tamanho definido

        T = insere_Arvore(T, x)  

    erd(T)
    print() # Quebra de linha entre as entradas
    del(T)