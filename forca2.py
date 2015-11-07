# coding: utf-8
# forca

acertos = []
pch = [0,0,0,0,0,0]
estado = 0
                                                  

animais = ["boi","vaca","lagartixa","dromedario","dinossauro","lagarto", \
           "formiga"]
comida = ["chocolate","macarrao","cuscuz", "tapioca", "miojo","queijo",\
        "feijao","milkshake","ketchup","pastilha","frango","carne"]
paises = ["dinarmarca","brasil","argentina", "espanha","uzbequistao", \
         "holanda", "canada", "chile"]
objeto = ["geladeira","monitor", "cadeira", "roupa", "teclado", "caneta", \
         "garfo", "processador", "placa", "oculos"]


categorias = {}
categorias ["Animais"] = animais
categorias ["Comidas"] = comida
categorias ["Paises"] = paises
categorias ["Objetos"] = objeto

categoria = raw_input("Escolha uma das categorias a seguir: Animais, \
Comidas, Paises, Objetos\n") 

from random import choice
palavra = choice(categorias[categoria])

for i in range(len(palavra)):
     acertos.append(0)

print " ____"
print " |  | "
print " |"
print " |"
print " |"
print "_|_"
print len(palavra) * "_ "

while True:
    letra = raw_input("Digite uma Letra: ")
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                acertos[i] = 1		
    else:
        pch[estado] = 1
        estado += 1
		
    print " ____"
    print " |  | "
    if pch[0] == 1:
        print " |  o"
    else:
        print " |"
    if pch[3] == 1:
        print " | /|\ "
    elif pch[2] == 1:
        print " | /|"
    elif pch[1] == 1:
        print " | /"
    else: 
        print " |"
    if pch[5] == 1:
        print " | / \ "
    elif pch[4] == 1:
        print " | /"
    else:
        print " |"
    print "_|_"

    for i in range(len(acertos)):
        if acertos[i] == 1:
            print palavra[i],
        else:
            print "_",
    if estado == 6:
        print "\nPerdeu, LOSER! A palavra era %s" % palavra
        break
    if 0 not in acertos:
        print "\nGanhou!"
        break
 
