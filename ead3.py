# Programador: Ricardo Abreu de Oliveira
# Professor: Eloi Araujo

#Criando a estrutura de um nó
class Noh(object):
    def __init__(self):
        self.info = None
        self.esq = None
        self.dire = None 


#Função para achar a distância da raiz
def posicao(r, l_erd):
    j = 0

    while l_erd[j] != r:
        j = j+1

    return j

#Função para criar Árvore Binária correspondente
def AB(l_red, l_erd):
    n =  len(l_red)

    if n == 0:
        return None

    j = posicao(l_red[0], l_erd)
    e = AB(l_red[1:j+1], l_erd[0:j+1])
    d = AB(l_red[j+1:n], l_erd[j+1:n])

    nova = Noh()
    nova.info = l_red[0]
    nova.esq = e
    nova.dire = d

    return nova 

#Função para percorrer e imprimir pela esquerda, direita e raiz (edr)
def edr(root):
    
    if root.info != None:
        
        if root.esq != None:
            edr(root.esq)
        
        if root.dire != None:   
            edr(root.dire)
        
        print(root.info, end ='')

l_red = []
l_erd = []

while True:
    try:
        l_red, l_erd = map(str, input().split())

        #Criando um objeto
        root = Noh()

        #Atribuindo a raiz 
        root = AB(l_red, l_erd)

        #Chamando a função para percorrer em edr
        edr(root)
        print()

    except EOFError:
        break