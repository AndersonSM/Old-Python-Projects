# coding: utf-8
# (De)Codificador by Anderson

dict = {'A': 'M' , 'B': 'N', 'C': 'O', 'D': 'P', 'E': 'Q', 'F': 'R', 'G': 'S',\
        'H': 'T', 'I': 'U', 'J': 'V' ,'L': 'X', 'K': 'Z', 'M': 'A', 'N': 'B',\
        'O': 'C', 'P': 'D', 'Q': 'E', 'R': 'F', 'S': 'G', 'T': 'H', 'U': 'I',\
        'V': 'J', 'X': 'L', 'Z': 'K', 'W': 'Y', 'Y': 'W', 'a': 'm' , 'b': 'n',\
        'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's', 'h': 't', 'i': 'u', \
        'j': 'v' ,'l': 'x', 'k': 'z', 'm': 'a', 'n': 'b', 'o': 'c', 'p': 'd', \
        'q': 'e', 'r': 'f', 's': 'g', 't': 'h', 'u': 'i', 'v': 'j', 'x': 'l', \
        'z': 'k', 'w': 'y', 'y': 'w'}

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

entrada = raw_input("Digite a frase a ser (de)codificada (sem acentos):\n")


somaspace = 0
strsoma = ""

for char in entrada:
    if char in alfabeto:
        strsoma += dict[char]
    else:
        strsoma += char
    if char == " ":
        somaspace += 1
    if somaspace == 5:
        strsoma += "\n"
        somaspace = 0            
        
f = open('texto.txt', 'w')
f.write(strsoma)
f.close()

print "\n Resultado: \n\n%s\n" % strsoma
print "\nUm arquivo de texto sera criado nesta pasta com os resultado da operaçao...\n"