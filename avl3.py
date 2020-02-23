#Programador: Ricardo Abreu de Oliveira

class Noh:
	def __init__(self, chave):
		self.pai = None
		self.esq = None
		self.dir = None
		self.chave = chave
		self.b = 0


def erd (p):
	if p == None:
		return

	else:
		if p.esq != None:
			erd(p.esq)

		#print(p.chave, '',end='')
		print(p.chave, "b:",p.b,)

		if p.dir != None:
			erd(p.dir) 


def red (p):
	if p == None:
		return None
	
	else:		
		print(p.chave, "b:",p.b,)
		#print(p.chave, '',end='')

		if p.esq != None:
			erd(p.esq)

		if p.dir != None:
			erd(p.dir) 	



def insere_sem_rotacao (p, x):
    novo = Noh(x)
    caminho = p

    direcao = 0

    if p == None and x != None:
    	return novo
    else:
	    if p.chave > x:
	    	p.esq = insere_sem_rotacao(p.esq, novo.chave)
	    	p.esq.pai = p	    	
    		p.b = p.b + 1
    		if p.pai != None and p.pai.esq == None:
    			p.pai.b = p.pai.b +1
	    		

	    else:
	    	p.dir = insere_sem_rotacao(p.dir, novo.chave)
	    	p.dir.pai = p
    		p.b = p.b - 1
    		if p.pai != None and p.pai.dir == None:
    			p.pai.b = p.pai.b -1
	    		
    return p						   


def insereAVL (p, x):
	novo = Noh(x)
	if p == None and x != None:
		return novo	
	else:
		if busca(p,x)	== None:					# se nao estiver na arvore
			if p.chave > x:
				p = rotacao(p)
				p.esq = insereAVL(p.esq, novo.chave)
				p.esq.pai = p
				p.b = p.b + 1
				if p.pai != None:
					p.pai.b = p.b + 1

			else:
				rotacao(p)
				p.dir = insereAVL(p.dir, novo.chave)
				p.dir.pai = p
				p.b = p.b - 1
				if p.pai != None:
					p.pai.b = p.b + 1

		else:
			return p
	return p	


def busca(p, x):
	if p == None:
		return None

	else:	
		if p.chave == x:
			q = p
			return q

		elif p.chave > x:
			return busca(p.esq, x)

		elif p.chave < x:
			return busca(p.dir, x)

def BuscaERemoveSemRotacao(p, x):

	flag =  busca(p, x)			# Flag recebe o endereço do noh a ser removido
	caminho = p 				# Caminho recebe raiz para percorrer a árvore
	caminho_volta = Noh(None)

	if flag == None:			# Se flag for nulo nao esta na arvore
		return None

	else:
		
		# Se flag for Folha
		#########################################
		if flag.esq == None and flag.dir == None:
			caminho_volta = flag                  				# Caminho para voltar da folha ate a raiz atualizando b

			if flag.pai.esq == flag:

				while caminho_volta.pai != None:				# Laco para voltar ate a raiz atualizando b
					if caminho_volta == caminho_volta.pai.esq:  # Se esq do pai do noh for o proprio noh b recebe -1
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:		# Se dir do pai do noh for o proprio noh b recebe +1
						caminho_volta.pai.b = caminho_volta.pai.b + 1							

					caminho_volta = caminho_volta.pai
				
				flag.pai.esq = None								# Atualizando esq de pai da folha

			elif flag.pai.dir == flag:
				while caminho_volta.pai != None:				# Laco para voltar ate a raiz atualizando b
					if caminho_volta == caminho_volta.pai.esq:
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:
						caminho_volta.pai.b = caminho_volta.pai.b + 1

					caminho_volta = caminho_volta.pai

				flag.pai.dir = None								# Atualizando dir de pai da folha
			
			del flag # Remocao da folha
			return
		#########################################

		# Se flag for um noh interno com esq Nulo
		#########################################
		if flag.esq == None and flag.dir != None:
			if flag.pai.esq == flag:							
				flag.pai.esq = flag.dir							# Atualizando pai

			elif flag.pai.dir == flag:							
				flag.pai.dir = flag.dir                         # Atualizando pai

			caminho = flag.dir									# Atualizando arvore
			del flag
		#########################################

		# Se flag for um noh interno com dir Nulo
		#########################################
		elif flag.dir == None and flag.esq != None:
			if flag.pai.esq == flag:							# Atualizando pai
				flag.pai.esq = flag.esq

			elif flag.pai.dir == flag:							# Atualizando pai
				flag.pai.dir = flag.esq

			caminho = flag.esq									# Atualizando arvore
			del flag
		#########################################	


		# Se flag for um noh interno sem campos nulos
		#########################################
		else:
			# Se nao for folha
			# Enquanto não encontrar um noh com dir nulo continua, pois o noh precisa
			# ser maior para manter a ordem  
			##################################################
			while caminho.dir != None:	
			
				if caminho.esq != None and caminho.chave >= x:
					caminho = caminho.esq

				elif caminho.dir != None and caminho.chave < x:
					caminho = caminho.dir
	
		
			##################################################

			# Ao encontrar uma folha faz a troca de valores, e atualiza os campos
			# O condicional >= determina que va para esq, logo temos que atualizar esq
			flag.chave = caminho.chave
			flag.esq = caminho.esq

			# caminho_volta recebe o caminho(endereco da folha) para voltar ate a raiz balanceando os nohs
			caminho_volta = caminho
			
			if caminho.pai.esq == caminho:							# Se esq do pai da folha for igual a folha, esq de pai passa a ser nulo
				
				while caminho_volta.pai != None:
					if caminho_volta == caminho_volta.pai.esq:
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:
						caminho_volta.pai.b = caminho_volta.pai.b + 1						

					caminho_volta = caminho_volta.pai				# Atualizando caminho de volta
				
				caminho.pai.esq = None

					

			elif caminho.pai.dir == caminho:						# Se dir do pai da folha for igual a folha, dir de pai passa a ser nulo

				while caminho_volta.pai != None:
					if caminho_volta == caminho_volta.pai.esq:
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:
						caminho_volta.pai.b = caminho_volta.pai.b + 1

					caminho_volta = caminho_volta.pai				# Atualizando caminho de volta

				caminho.pai.dir = None


			del caminho
	return			


def BuscaERemoveAVL(p, x):

	flag =  busca(p, x)			# Flag recebe o endereço do noh a ser removido
	caminho = p 				# Caminho recebe raiz para percorrer a árvore
	caminho_volta = Noh(None)
	aux = None
	r = None

	r = rotacao(flag)  #Faz a rotacao
	flag = busca(r, x)

	if flag == None:			# Se flag for nulo nao esta na arvore
		return None

	else:
		
		# Se flag for Folha
		#########################################
		if flag.esq == None and flag.dir == None:
			caminho_volta = flag  
			aux = flag                				# Caminho para voltar da folha ate a raiz atualizando b

			if flag.pai.esq == flag:

				while caminho_volta.pai != None:				# Laco para voltar ate a raiz atualizando b
					if caminho_volta == caminho_volta.pai.esq:  # Se esq do pai do noh for o proprio noh b recebe -1
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:		# Se dir do pai do noh for o proprio noh b recebe +1
						caminho_volta.pai.b = caminho_volta.pai.b + 1							

					caminho_volta = caminho_volta.pai
				
				flag.pai.esq = None								# Atualizando esq de pai da folha

			elif flag.pai.dir == flag:
				while caminho_volta.pai != None:				# Laco para voltar ate a raiz atualizando b
					if caminho_volta == caminho_volta.pai.esq:
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:
						caminho_volta.pai.b = caminho_volta.pai.b + 1

					caminho_volta = caminho_volta.pai

				flag.pai.dir = None								# Atualizando dir de pai da folha
			
			del flag # Remocao da folha
			#r = rotacao(aux)  #Faz a rotacao
		#########################################

		# Se flag for um noh interno com esq Nulo
		#########################################
		if flag.esq == None and flag.dir != None:
			if flag.pai.esq == flag:							
				flag.pai.esq = flag.dir							# Atualizando pai

			elif flag.pai.dir == flag:							
				flag.pai.dir = flag.dir                         # Atualizando pai

			caminho = flag.dir									# Atualizando arvore
			aux = flag
			del flag
			#r = rotacao(aux)  #Faz a rotacao
		#########################################

		# Se flag for um noh interno com dir Nulo
		#########################################
		elif flag.dir == None and flag.esq != None:
			if flag.pai.esq == flag:							# Atualizando pai
				flag.pai.esq = flag.esq

			elif flag.pai.dir == flag:							# Atualizando pai
				flag.pai.dir = flag.esq

			caminho = flag.esq									# Atualizando arvore
			aux = flag
			del flag
			#r = rotacao(aux)
		#########################################	


		# Se flag for um noh interno sem campos nulos
		#########################################
		else:
			# Se nao for folha
			# Enquanto não encontrar um noh com dir nulo continua, pois o noh precisa
			# ser maior para manter a ordem  
			##################################################
			while caminho.dir != None:	
			
				if caminho.esq != None and caminho.chave >= x:
					caminho = caminho.esq

				elif caminho.dir != None and caminho.chave < x:
					caminho = caminho.dir
	
		
			##################################################

			# Ao encontrar uma folha faz a troca de valores, e atualiza os campos
			# O condicional >= determina que va para esq, logo temos que atualizar esq
			flag.chave = caminho.chave
			flag.esq = caminho.esq
			aux = flag

			# caminho_volta recebe o caminho(endereco da folha) para voltar ate a raiz balanceando os nohs
			caminho_volta = caminho
			
			if caminho.pai.esq == caminho:							# Se esq do pai da folha for igual a folha, esq de pai passa a ser nulo
				
				while caminho_volta.pai != None:
					if caminho_volta == caminho_volta.pai.esq:
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:
						caminho_volta.pai.b = caminho_volta.pai.b + 1						

					caminho_volta = caminho_volta.pai				# Atualizando caminho de volta
				
				caminho.pai.esq = None

					

			elif caminho.pai.dir == caminho:						# Se dir do pai da folha for igual a folha, dir de pai passa a ser nulo

				while caminho_volta.pai != None:
					if caminho_volta == caminho_volta.pai.esq:
						caminho_volta.pai.b = caminho_volta.pai.b - 1

					elif caminho_volta == caminho_volta.pai.dir:
						caminho_volta.pai.b = caminho_volta.pai.b + 1

					caminho_volta = caminho_volta.pai				# Atualizando caminho de volta

				caminho.pai.dir = None


			del caminho
			#r = rotacao(aux) # Faz a rotacao
	return r

def RD(p):
	# Auxilia a guardar subarvore esquerda de p
	aux = p.esq


	p.esq = aux.dir 		# Atualiza a esquerda da raiz atual
	aux.dir.pai = p 		# pai da subarvore direita se torna p
	p.pai = aux 			# Atualiza a nova raiz

	aux.dir = p 			# Subarvore direita agora eh p 
	aux.pai = None			# atualizando pai da raiz(Nulo)

	return aux 				# Retornando nova raiz


def DRD(p):
	aux1 = p.esq 			# aux1 eh subarvore esq de p
	aux2 = aux1.dir 		# aux2 eh subarvore direita de aux1 ou p.esq.dir
	
	# Rotacao a esquerda
	#####################
	aux1.dir = aux2.esq 	
	aux2.pai = aux1.pai 	# o pai de aux2 passa a ser a raiz (pai de aux1)
	aux1.pai = aux2 		# Atualiza pai de aux1 para aux2
	aux2.esq = aux1 		# Terminando a rotacao a esquerda

	# Rotacao a direita
	#####################
	p.esq = aux2.dir

	p.pai = aux2			# atualizando pai de p

	aux2.dir = p			# rotaciona aux2, direita de aux2 agora eh p

	aux2.p = None			# Atualizando o pai da nova(Nulo)

	return aux2				# Retornando nova raiz


def RE(p):

	aux = p.dir

	p.dir = aux.esq
	aux.pai = p.pai
	p.pai = aux
	aux.esq = p

	return aux


def DRE(p):
	aux1 = p.dir
	aux2 = aux1.esq

	aux1.esq =  aux2.dir
	aux2.pai = aux1.pai
	aux2.dir = aux1
	aux1.pai = aux2

	p.dir = aux2.esq
	aux2.pai = p.pai
	aux2.esq = p
	p.pai = aux2

	return aux2


def rotacao(p):
		
	if p.b == 2 and p.esq.b == 1: #RD
		root = RD(p)
			
		root.b = 0					# Ajuste de balanceamento pela tabela
		root.dir = 0				
		return root
		

	elif p.b == -2 and p.dir.b == -1:	#RE
		root = RE(p)
			
		root.b = 0
		root.esq.b = 0
		return root
		
		
	elif p.b == 2 and p.esq.b == 0:	#RD
		root = RD(p)
			
		root.b = -1
		root.dir.b = 1
		return root
		
		
	elif p.b == -2 and p.dir.b == 0:	#RE
		root = RE(p)
			
		root.b = 1
		root.esq.b = -1
		return root
		
		
	elif p.b == 2 and p.esq.b == -1 and p.esq.dir.b == -1: #DRD
		root = DRD(p)
			
		root.b = 0
		root.esq.b = 1
		root.dir.b = 0
		return root
		
		
	elif p.b == 2 and p.esq.b == -1 and p.esq.dir.b == 0: #DRD
		root = DRD(p)
			
		root.b = 0
		root.esq.b = 0
		root.dir.b = 0
		return root
		
		
	elif p.b == 2 and p.esq.b == -1 and p.esq.dir.b == 1: #DRD
		root = DRD(p)

		root.b = 0
		root.esq.b = 0
		root.dir.b = -1
		return root


	elif p.b == -2 and p.dir.b == 1 and p.dir.esq.b == -1: #DRE
		root = DRE(p)

		root.b = 0
		root.dir.b = 0
		root.esq.b = 1
		return root
		
	elif p.b == -2 and p.dir.b == 1 and p.dir.esq.b == 0: #DRE
		root = DRE(p)

		root.b = 0
		root.dir.b = 0
		root.esq.b = 0
		return root


	elif p.b	== -2 and p.dir.b == 1 and p.esq.dir.b == 1: #DRE
		root = DRE(p)

		root.b = 0
		root.dir.b = -1
		root.esq.b = 0
		return root
	return p	


# 'Main'
p = None
n  = int(input())

for i in range(n):
	entrada = int(input())
	p = insere_sem_rotacao(p, entrada)
#Entrada do número a ser buscado
x = int(input())
root = BuscaERemoveAVL(p,x)

# Impressao rotacao
#r = rotacao(p)
erd(root)
print()
