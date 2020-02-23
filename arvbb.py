# Programador: Ricardo Abreu de Oliveira

class No:
    def __init__ (self, info):
        self.info = info
        self.pai = self.dir = self.esq = None

def red(T):
    if T != None:
        print(T.info,"" ,end='')

        if T.esq != None:
            red(T.esq)

        if T.dir != None:
            red(T.dir)    

# Recursão para imprimir em ordem simétrica
def erd(T):
    if T != None:
        if T.esq != None:
            erd(T.esq)

        # Método para imprimir na mesma linha com espaço entre as palavras,
        # porém fica com espaço na última palavra 
        print(T.info, '', end='')        
        
        if T.dir != None:
            erd(T.dir)

# Recursão para imprimir em ordem Pós-ordem
def der(T):
    
    if T.info != None:
        
        if T.esq != None:
            der(T.esq)
        
        if T.dir != None:   
            der(T.dir)
        
        print(T.info,"", end='')


def insere_Arvore (T, x):
    if T == None and x != None:
        return x

    novo = No(x.info)
        
    if T.info > novo.info:
        T.esq = insere_Arvore(T.esq, novo)

    else:
        T.dir = insere_Arvore(T.dir, novo)

    return T   #retorna o novo nó na posição certa     
        


  

cont = int(input())

for k in range(cont):               #Contador de entradas
    n = int(input())                # Num de entradas

    T = None
    
    entrada = input().split()       #Entrada divida e colocada em um vetor
   
    for i in range(n):              #Para cada item no vetor é criado um objeto e inserido
      
        x = No(int(entrada[i]))     
        T = insere_Arvore(T, x)     
        
    #print("Case",k+1,':')
    print('Case {0:%d}:'.format(k+1))
    
    print("Pre.: ",end='')
    red(T)    

    print('\n')

    print("In.: ",end='')
    erd(T)

    print('\n')

    print("Pos.: ",end='')
    der(T)

    print('\n')
        
    print() # Quebra de linha entre as entradas
    print()
    
    del(T)
    entrada = None