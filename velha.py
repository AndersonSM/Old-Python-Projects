tabuleiro = []
for linha in range(3):
	tabuleiro.append([])
	for coluna in range(3):
		tabuleiro[linha].append(" ")
vencedor = False
jogador = 1
def printar_tabuleiro():
	for linha in range(3):
		for coluna in range(3):
			print tabuleiro[linha][coluna],
			if coluna != 2:
				print "|",
			else:
				print ""
		if linha != 2:
			print "-----------"
while(not vencedor):
	jogador += 1
	if jogador > 9:
		printar_tabuleiro()
		print "DEU VELHA!!"
		break
	printar_tabuleiro()
	if jogador % 2 == 0:
		vez = "X"
		print "Jogador 1"
	else:
		vez = "O"
		print "Jogador 2"
	valida = False
	while(not valida):
		linha = int(raw_input("Digite a linha\n"))-1
		coluna = int(raw_input("Digite a coluna\n"))-1
		if tabuleiro[linha][coluna] == " " and 0 <= linha <= 2 and 0 <= coluna <= 2:
			valida = True
			break
		print "Espaco preenchido ou coordenadas invalidas"
	tabuleiro[linha][coluna] = vez
	for linha in range(3):
		if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] and tabuleiro[linha][0] != " ":
			vencedor = True
	for coluna in range(3):
		if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[2][coluna] != " ":
			vencedor = True
	if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
		vencedor = True
	if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
		vencedor = True
	if vencedor:
		printar_tabuleiro()
		if linha != 2:
			print "-----------"
		if vez == "X":
			print "JOGADOR 1 VENCEU!!!"
		else:
			print "JOGADOR 2 VENCEU!!!"
		
