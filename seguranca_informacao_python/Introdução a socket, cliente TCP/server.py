#servidor UDP
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso")

host = ('localhost')
porta = 5433

#bind faz a ligação entre clinte-servidor através do host e da porta

s.bind((host, porta))
 
mensagem = "Servidor: Olá"

while 1:
    dados, endereço = s.recvfrom(1024)
    if dados:
        print('Servidor enviando mensagem')
        #enviando mensagem via pacotes udp
        s.sendto(dados + (mensagem.ecode()), endereço) 

#Primeiro rodamos o server e depois rodamos o cliente