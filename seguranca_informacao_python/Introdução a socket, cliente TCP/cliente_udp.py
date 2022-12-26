 #udp = user datagram protocol. Parecido com o tcp. Também está na camada de transporte. 
# Permite o envio de datagramas por pacotes ipv4 ou ipv6, mas sem verificação de integridade, mas sim de disponibilidade. Verifica se o hosp está recebendo dados. 
# Contempla o princípio de disponibilidade.
import socket
#UDP é o protocoo de anagrama do cliente
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ('Cliente criado com sucesso')
host = ('localhost')
porta = 5433
msg = ( 'Olá')

try: 
    print ('Cliente '+ msg)
    #encode = empacotando a msg e enviando nos pacoes udp
    s.sendto(msg.encode(), (host, porta,))
    #esperando uma resposta de 1024 bite
    dados, sevidor = s.recvfrom(1024)
    dados = dados.decode()
    print ("Cliente: "+dados)
finally:
    print ('Cliente fechando a conexão')
    s.close()