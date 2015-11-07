# coding: utf-8

import os
import platform

# Importa o .txt com o dic dos contatos ou cria o .txt
try:
    f = open('contatos.txt', 'r')
    f.close()
    print "Contatos importados com sucesso."
except:
    f = open('contatos.txt', 'w')
    f.write("{}")
    f.close()

f = open('contatos.txt', 'r')    
contatos = eval(f.read())
f.close()

# Funções
def print_info():
    print "Esta agenda possui as seguintes funções:\n\
 -Inserir contato\n -Deletar contato -Buscar contato\n\
 -Mostrar todos os contatos\n -Salva e fecha a agenda\n\
Para mais informações, digite:\n\
 '+info'\n 'função' (inserir, buscar, deletar, mostrar, salvar)\n"

def info_inserir():
    print "Para inserir um contato na agenda, digite\n\
'inserir'. Em seguida, digite a quantidade de contatos que serão inseridos.\n\
Nas seguintes linhas, digite: 'Nome do contato: Número'.\n\
Exemplo: inserir\n\
         2\n\
         Joaquim: 3214-9876\n\
         Maria: 1234-5678\n"
    
def info_buscar():
    print "Para buscar um contato na agenda, digite:\n\
 buscar\n 'nome do contato'\n"

def info_del():
    print "Para deletar um contato da agenda, digite:\n\
 deletar\n 'nome do contato'\n"

def info_mostrar():
    print "Para exibir todos os contatos da agenda, digite:\n\
 'imprimir' ou 'mostrar'\n"

def info_salvar():
    print "Para salvar e fechar agenda, digite:\n\
 'finalizar'\n"

def inserir(contatos):
    while True:
        try:
            qtd = int(raw_input("Quantos contatos você deseja inserir?\n"))
            print ""
            break
        except:
            print "Digite um número válido!\n"
    for i in range(qtd):
        while True:
            try:
                entrada = raw_input("Insira o %dº contato:\n" % (i+1)).title().strip().split(": ")
                contatos[entrada[0].strip()] = entrada[1].strip()
                print ""
                break
            except IndexError:
                print "\nEntrada digitada de forma errada. Tente novamente.\n"
    print "Os contatos foram inseridos na agenda com sucesso.\n"

def deletar(contatos):
    while True:
        contato = raw_input("Digite o nome do contato a ser deletado:\n").title().strip()
        if contato in contatos:
            del contatos[contato]
            print "Contato deletado com sucesso.\n\n"
            break
        else:
            print "O contato '%s' não consta na agenda.\n" % contato

def buscar(procurado, contatos):
    if contatos.has_key(procurado):
            print "----------"
            print "O telefone de %s é: %s" % (procurado, contatos[procurado])
            print "----------\n"
    else:
        print "----------"
        print "Contato inexistente"
        print "----------\n"

def imprimir(contatos):
    # Cria uma lista pra ordenar os contatos em ordem alfabética
    if contatos != {}:
        """lista = []
        for nome in contatos:
            lista.append(nome)
        lista.sort()"""
        
        lista = contatos.keys()
        lista.sort()
        for e in lista:
            print "----------"
            print "Nome: %s" % e
            print "Fone: %s" % contatos[e]
            print "----------"
    else:
        print "Nenhum contato salvo.\n"

def salvar(contatos):
    f = open('contatos.txt', 'w')
    f.write(str(contatos))
    f.close()
    print "Os contatos foram salvos com sucesso.\n"

def limpa_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print_info()

# Principal
print_info()

while True:    
    entrada = raw_input().lower().strip()
    
    if entrada == "finalizar" or entrada == "salvar":
        salvar(contatos)
        break
        
    elif entrada == "+info":
        funcao = raw_input().lower().strip()
        if funcao == "inserir":
            limpa_tela()
            info_inserir()
        elif funcao == "buscar":
            limpa_tela()
            info_buscar()
        elif funcao == "deletar":
            limpa_tela()
            info_del()
        elif funcao == "mostrar":
            limpa_tela()
            info_mostrar()
        elif funcao == "salvar":
            limpa_tela()
            info_salvar()
        else:
            print "\nFunção inválida\n"

    elif entrada == "inserir":
        limpa_tela()
        inserir(contatos)
    
    elif entrada == "deletar":
        limpa_tela()
        deletar(contatos)
    
    elif entrada == "buscar":
        limpa_tela()
        procurado = raw_input("Digite o nome do contato a ser procurado:\n").title().strip()
        buscar(procurado, contatos)
        
    elif entrada == "imprimir" or entrada == "mostrar":
        limpa_tela()
        imprimir(contatos)
    
    else:
        print "\nFunção inválida. Tente novamente.\n"