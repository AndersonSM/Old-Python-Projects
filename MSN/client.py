# coding: utf-8

import socket

ip = "192.168.0.105"
port = 5005
buffersize = 1024

nome_do_cliente = raw_input("Digite seu nome: ")

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	msg = raw_input("Digite a mensagem: ")
	s.send(nome_do_cliente + "***" + msg)
	data = s.recv(buffersize).split("***")
	print data[0], "enviou:", data[1]
	s.close()
