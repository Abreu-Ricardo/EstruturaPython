# Programador: Ricardo Abreu de Oliveira
# Professor: Eloi Araujo

#Criando a estrutura de um nó
class Noh(object):
	def __init__(self):
		self.info = None
		self.pai = None
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
	nova.pai = None
	nova.esq = e
	nova.dire = d

	return nova	

#Função para percorrer e imprimir pela direita, esquerda e raiz(der)
def der(root):
	
	if root.info != None:
		
		if root.esq != None:
			der(root.esq)
		
		if root.dire != None:	
			der(root.dire)
		
		print(root.info)


l_red = ['E', 'F', 'A', 'B', 'C', 'D', 'G', 'H', 'I', 'J']
l_erd = ['A', 'F', 'C', 'B', 'D', 'E', 'G', 'I', 'H', 'J']

#Criando um objeto
root = Noh()

#Atribuindo a raiz 
root = AB(l_red, l_erd)

#Chamando a função para percorrer em der
der(root)