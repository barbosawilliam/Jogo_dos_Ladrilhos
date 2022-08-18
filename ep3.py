def funcaoZero (tabuleiroInicial, tabuleiroFinal):
	if (tabuleiroInicial == tabuleiroFinal):
		return "SIM"
	else:
		return "NAO"

def ehValido (movimento, tabuleiroInicial, Izero, Jzero):
	if (movimento == "c"):
		if (Izero == 0):
			return False
		else:
			return True
	elif (movimento == "b"):
		if (Izero == len(tabuleiroInicial) - 1):
			return False
		else:
			return True
	elif (movimento == "d"):
		if (Jzero == len(tabuleiroInicial) - 1):
			return False
		else:
			return True
	elif (movimento == "e"):
		if (Jzero == 0):
			return False
		else:
			return True

def funcaoUm (tabuleiroInicial, lista):
	Izero = 0
	Jzero = 0
	for i in range(len(tabuleiroInicial)):
		for j in range(len(tabuleiroInicial)):
			if (tabuleiroInicial[i][j] == '0'):
				Izero = i
				Jzero = j

	for i in range(len(lista)):
		if (ehValido (lista[i], tabuleiroInicial, Izero, Jzero)): #Se é possível fazer o movimento, então mover
			if (lista[i] == "c"):
				temp = tabuleiroInicial[Izero - 1][Jzero]
				tabuleiroInicial[Izero - 1][Jzero] = 0
				tabuleiroInicial[Izero][Jzero] = temp
				Izero = Izero - 1
			elif (lista[i] == "b"):
				temp = tabuleiroInicial[Izero + 1][Jzero]
				tabuleiroInicial[Izero + 1][Jzero] = 0
				tabuleiroInicial[Izero][Jzero] = temp
				Izero = Izero + 1
			elif (lista[i] == "d"):
				temp = tabuleiroInicial[Izero][Jzero + 1]
				tabuleiroInicial[Izero][Jzero + 1] = 0
				tabuleiroInicial[Izero][Jzero] = temp
				Jzero = Jzero + 1
			elif (lista[i] == "e"):
				temp = tabuleiroInicial[Izero][Jzero - 1]
				tabuleiroInicial[Izero][Jzero - 1] = 0
				tabuleiroInicial[Izero][Jzero] = temp
				Jzero = Jzero - 1
		else:
			return ["NAO", i]

	return ["SIM"]

def ladrilho (Mat, Matfim, p, pmax, pos, mov, ListaMov): #Pos = posição que está o 0 = lista com duas posições [linha, coluna]
#Mov é o último movimento, ListaMov é uma lista com todos os movimentos realizados

	if (funcaoZero (Mat, Matfim) == "SIM"):
		return True
	else:
		return False

def main():
	print("Opcao de jogo: ")
	opcaoJogo = int(input())
	print("Tamanho do tabuleiro: ")
	n = int(input())
	tabuleiroInicial = []
	
	if (opcaoJogo == 0):
		print("Tabuleiro inicial: ", end = "")
		for i in range(n):
			entrada = input()
			lista = entrada.split(" ")
			tabuleiroInicial.append(lista)

		tabuleiroFinal = []
		print("Tabuleiro final: ", end = "")
		for i in range(n):
			entrada = input("")
			lista = entrada.split(" ")
			tabuleiroFinal.append(lista)
		print(funcaoZero(tabuleiroInicial, tabuleiroFinal))	

	elif (opcaoJogo == 1):
		print("Tabuleiro inicial: ")
		for i in range(n):
			entrada = input()
			lista = entrada.split(" ")
			tabuleiroInicial.append(lista)

		print("Digite seq mov: ")
		listaMovimentos = input()
		resultado = funcaoUm (tabuleiroInicial, listaMovimentos)
		if (resultado[0] == "NAO"):
			print("%s: %d" %(resultado[0], resultado[1] + 1))
		else:
			print("Tabuleiro final: ")
			for i in range(n):
				for j in range(n):
					print("%d " %int(tabuleiroInicial[i][j]), end = "")
				print()

	elif (opcaoJogo == 2):
		pmax = int(input("Digite a profundidade maxima: "))
		print("Tabuleiro inicial: ", end = "")
		for i in range(n):
			entrada = input("")
			lista = entrada.split(" ")
			tabuleiroInicial.append(lista)
		tabuleiroFinal = []
		print("Tabuleiro final: ", end = "")
		for i in range(n): #Pegando o tabuleiro final
			entrada = input("")
			lista = entrada.split(" ")
			tabuleiroFinal.append(lista)




main()