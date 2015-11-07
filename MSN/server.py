# coding: utf-8

import socket

ip = "192.168.0.105"
port = 5005
buffersize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)

nome_do_cliente = raw_input("Digite seu nome: ")

while True:
	conn, addr = s.accept()
	data = conn.recv(buffersize).split("***")
	print data[0], "enviou:", data[1]
	msg = raw_input("Enviar mensagem de volta: ")
	conn.send(nome_do_cliente + "***" + msg)
	
