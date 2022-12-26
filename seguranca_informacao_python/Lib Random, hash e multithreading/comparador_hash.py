import hashlib
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1=hashlib.new('ripemd160') #aqui escolhemos o tipo de verificador de hash
hash1.update(open(arquivo1, 'rb').read())#faz a comparação do hash #rb é um método de leitura (reab/binary)
hash2=hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())#faz a comparação do hash #rb é um método de leitura (reab/binary)

if hash1.digest() != hash2:
#função digeste resume os dados passados pra o método update
    print(f'O arquivo {arquivo1} é diferente do arquivo {arquivo2}.')
else:
    print(f'O arquivo {arquivo1} é igual aoarquivo  {arquivo2}.')

print (f'Primeiro hash: {hash1} | Segundo hash: {hash2}')