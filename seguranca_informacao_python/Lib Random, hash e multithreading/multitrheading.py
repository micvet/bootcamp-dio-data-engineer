#Executar mais de uma tarefa simultaneamente
from threading import Thread
import time
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print (f'Piloto: {piloto},Km{trajeto}')
        trajeto+=velocidade
        time.sleep(0.5)


#Apesar da velocidade do carro 2 ser maior, a tarefa é executada depois, pois os processos não ocorrem simultaneamente.
#Para evitar isso, vamos usar o thread
t_carro1= Thread(target=carro, args=['Ayrton',1])
t_carro2= Thread(target=carro, args=['Felipe', 2])
t_carro1.start #startar o comando thread
t_carro2.start