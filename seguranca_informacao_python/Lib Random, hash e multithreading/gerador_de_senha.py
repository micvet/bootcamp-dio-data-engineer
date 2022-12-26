#biblioteca random
#Este módulo implementa geradores de números, letras e simbolos  pseudoaleatórios para várias distribuições.

#Hash
#Python oferece um hash() método para codificar os dados em um valor irreconhecível.
#Sintaxe: hash (obj)


#multithreading
#Multithreading refere-se à execução simultânea de vários threads, alternando rapidamente o controle da CPU entre os threads (chamado de troca de contexto) 
#O Python Global Interpreter Lock limita a execução de um thread por vez, mesmo que a máquina contenha vários processadores.

#ipaddress
#ipaddress fornece os recursos para criar, manipular e operar em redes e endereços IPv4 e IPv6

import random
import string 


tamanho = input ('Digite a quantidade de caracteres da senha: ')
#ascii_letters= gera letras maiúsculas e minúsculas / digits (0-9) / 
char = string.ascii_letters + string.digits + '!@#$%&*()-=+'

rnd = random.SystemRandom() 

print (''.join(rnd.choice(char) for i in range (tamanho)))

