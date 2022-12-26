#biblioteca socket permite o acesso de baixo nível à interface de rede
#TCP= transmission control protocol. Dá suporte à rede global de internet e verifica integridade dos dados
import socket 
import sys 
#Fornece acesso a alguma variaveis e funções que tem interação com o inteerpretador - python

#funcão para tentar uma conexao TCP/IP
def main():
    try:
        #parametros inseridos: 1 - family - familia de protocolo usada: protocolo IP, 2- tipo:TCP e 3- protocolo: TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print ("A conexão falhou")
        print (f"Erro: {e}")
        sys.exit()

    print ("Socket criado com sucesso.")

    #Definindo host alvo:
    host_alvo = input("Digite o host de destino:  " )
    porta_alvo = int(input ("Digite a porta a ser conectada: "))
    
    #conectando. Caso a conexão ocorra com sucesso, ela durará 2 segundo para não entrar em loop
    try:
        s.connect((host_alvo, porta_alvo))
        print (f"Cliente TCP conectado com sucesso no host {host_alvo} e porta {porta_alvo}!")
        s.shutdown(2)
    except socket.error as e:
        print (f'Não foi possível estabelecer uma conexão ao host {host_alvo}.')
        print (f"Erro: {e}")
        sys.exit()

if __name__ == "__main__":
    main()






