import ipaddress

ip= "192.168.0.0/24"

#rede = ipaddress.ip_address(ip) #imprimindo o ip  
#print (rede+100)
#a função ip_network possbilita o uso do parâmetro stric
rede = ipaddress.ip_network(ip, strict=False)#strict=false: para fazer com que qqr numero de rede seja aceito
print (rede)
