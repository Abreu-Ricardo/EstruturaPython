#treino em Python
def main():
	V = []
	num_de_itens = int(input("Número de itens do array:"))

	for i in range(0,num_de_itens):
		x = int(input())
		V.append(x)
	#V.sort()
	for i in range(0, num_de_itens):
		print(V[i])	
main()