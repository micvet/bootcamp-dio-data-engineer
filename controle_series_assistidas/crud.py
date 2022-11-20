import mysql.connector

iniciar = True

while iniciar == True:

    conexao = mysql.connector.connect(
    host='localhost',
    database='movies_controll',
    user='root',
    password=''
    )

    opt = [1,2,3,4,5]
    opcoes = int(input("***********************************************************\nControle de séries e filmes assistidos\n\nDigite a opção desejada:\n\n 1) Visualizar séries e filmes cadastrados\n 2) Inserir nova série/filme\n 3) Editar registro \n 4) Deletar registro \n 5) Sair\n\n ***********************************************************\n"))
        
    while opcoes not in opt:
        print ("Digite uma opção válida!")
        opcoes = int(input("***********************************************************\nControle de séries e filmes assistidos\n\nDigite a opção desejada:\n\n 1) Visualizar séries e filmes cadastrados\n 2) Inserir nova série/filme\n 3) Editar registro \n 4) Deletar registro \n 5) Sair\n\n ***********************************************************\n"))
        
    if opcoes == 1:
        select = ("SELECT * FROM movies;")
        cursor = conexao.cursor()
        cursor.execute(select)
        linhas = cursor.fetchall()
        for linha in linhas:
            print ("************************************")
            print("Id:", linha[0])
            print("Tipo:", linha[1])
            print("Nome:", linha[2])
            print("Qtde Episódios:", linha[3])
            print("Episódios assistidos:", linha[4])
            print("Nota:", linha[5])
            print("Última visualização:", linha[6])
            print ("************************************")
        print("Visualização/alteração encerrada!")
        iniciar = True
    
        
    elif opcoes == 2:
        tipo = str(input('Digite 0 para série ou 1 para filme: '))
        categoria = ['0','1']
        while tipo not in categoria:
            print ('Opção inválida. Digite 0 para série ou 1 para filme: ')
            tipo = str(input('Digite 0 para série ou 1 para filme: '))
       
        nome_serie = input('Insira o nome da série ou filme: ')
        
        total_ep = int(input('Insira o número total de episódios:  '))
        episodios_assistidos = int(input('Insira quantos episódios já assistiu: '))
        last_view = input('Insira a data da última visualização, no formato aaaa-mm-dd: ')
        nota = int(input('Digite sua nota para a série: '))
        insert = (f"INSERT INTO movies (tipo, nome, total_ep, atual_ep, nota, last_view) VALUES ('{tipo}','{nome_serie}',{total_ep},{episodios_assistidos},{nota},'{last_view}')")
         
        cursor = conexao.cursor()
        cursor.execute(insert)
        conexao.commit()
        print("Dados inseridos com sucesso!")
        iniciar = True
    
    elif opcoes == 3:
        
        opcoes = {1:'tipo',2:'nome',3:'total_ep',4:'atual_ep',5:'nota',6:'last_view'}
        registro_alterar = int(input('Digite o ID do registro que deseja alterar: '))
        opcao_alter = int(input('\nAlterar:\n1) Tipo \n2) Nome \n3) Total de episódios \n4)Episódio atual \n5) Nota \n6)Última visualização\n'))
        
        while opcao_alter not in opcoes.keys():
            print ("Digite uma opção válida!")
            opcao_alterar = int(input('\nAlterar:\n1) Tipo \n2) Nome \n3) Total de episódios \n4)Episódio atual \n5) Nota \n6)Última visualização\n'))
        
        novo_registro = input ('Insira o novo registro: ')    
        setar = opcoes[opcao_alter]
        alter = (f"UPDATE movies SET {setar} = {novo_registro} WHERE id = {registro_alterar};")
        print (alter)
        
        cursor = conexao.cursor()
        cursor.execute(alter)
        conexao.commit()
        print("Alteração realizada com sucesso!")
        iniciar = True
        
    elif opcoes == 4:
        registro_deletar = int(input('Digite o ID do registro que deseja deletar: '))
        delete = (f"DELETE FROM movies WHERE id = {registro_deletar} LIMIT 1;")
        print (delete)
        cursor = conexao.cursor()
        cursor.execute(delete)
        conexao.commit()
        print ("Registro excluído com sucesso.")
        iniciar = True

    else:
        iniciar = False
        cursor = conexao.cursor()
        conexao.close()
        print("Obrigada por utilizar nosso aplicativo!")

  
    def visualizar():
        select = ("SELECT * FROM movies;")
        return select
        
    def inserir():
        nome_serie = input('Insira o nome da sua série')
        tipo = input('Digite 0 para série ou 1 para filme: ')
        total_ep = int(input('Insira o número total de episódios '))
        episodios_assistidos = int(input('Insira quantos episódios já assistiu'))
        last_view = input('Insira a data da última visualização, no formato aaaa-mm-dd')
        nota = int(input('Digite sua nota para a série: '))
        insert = (f"INSERT INTO movies (tipo, nome, total_ep, atual_ep, nota, last_view) VALUES ('{tipo}','{nome_serie}','{total_ep}','{episodios_assistidos}','{nota}'")
        return insert

    def alterar():
        options = [1,2,3,4,5,6]
        registro_alterar = int(input('Digite o ID do registro que deseja alterar: '))
        opcao_alter = input('Alterar\n1) Tipo \n2) Nome \n3) Total de episódios \n4)Episódio atual \n5) Nota \n6)Última visualização')
        while opcao_alterar not in options:
            print ("Digite uma opção válida!")
            opcao_alterar = int(input('Alterar\n1) Tipo \n2) Nome \n3) Total de episódios \n4)Episódio atual \n5) Nota \n6)Última visualização'))
        
        novo_registro = input ( 'Digite o novo registro: ')    
        if opcao_alter == 1:
            alter = (f"'ALTER TABLE movies set tipo = '{novo_registro}' WHERE id = {registro_alterar} LIMIT 1;")
        
        elif opcao_alter == 2:
            alter = (f"'ALTER TABLE movies set nome = '{novo_registro}' WHERE id = {registro_alterar} LIMIT 1;")
            return alter

        elif opcao_alter == 3:
            alter = (f"'ALTER TABLE movies set total_ep = {novo_registro} WHERE id = {registro_alterar} LIMIT 1;")
            return alter

        elif opcao_alter == 4:
            alter = (f"'ALTER TABLE movies set tipoatual_ep = {novo_registro} WHERE id = {registro_alterar} LIMIT 1;")
            return alter

        elif opcao_alter == 5:
            alter = (f"'ALTER TABLE movies set nota = {novo_registro} WHERE id = {registro_alterar} LIMIT 1;")
            return alter

        else:
            alter = (f"'ALTER TABLE movies set last_view = '{novo_registro}' WHERE id = {registro_alterar} LIMIT 1;")
            return alter

    def deletar():
        
        registro_deletar = int(input('Digite o ID do registro que deseja deletar: '))
        delete = (f"'DELETE FROM movies WHERE id = {registro_deletar} LIMIT 1;")
        return delete

    def sair():
        desconect = conexao.close()
        return desconect

    def menu():
        import mysql.connector
          
    def executar():
        menu()
        cursor = conexao.cursor()
        cursor.execute()
        conexao.commit()
        print("Visualização/alteração encerrada!")
        conexao.close()




        


