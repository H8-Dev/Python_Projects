# Variavel global essencial.
biblioteca = []


#<-------------------------------------------------------------------------->
#<------------------------- COMANDOS DE PREPARAÇÃO ------------------------->
#<-------------------------------------------------------------------------->


def data_prep(): #Prepara os dados para serem usados, lendo o banco e armazenando as informações na memória
    biblioteca.clear() #Limpa a memória para evitar repetições
    with open("banco.csv", "r", encoding="utf-8") as banco:
        for a in banco.readlines()[1:]:
            linha = a.split(",")
            biblioteca.append(linha)
        banco.close()


def float_check(price): #Verifica se o valor inserido é um número decimal, caso contrário pede para inserir novamente
    try:
        float(price)
        return round(float(price), 2)
    except ValueError:
        return None


def game_check(name): #Verifica se o nome do jogo já existe no banco, caso exista invalida o insert
    cont = 0
    key = 1

    while(key == 1 and cont < len(biblioteca)):

        if(name == biblioteca[cont][0]):
            print("Jogo já existe no banco. Insira um jogo válido")
            check = False
            key = 0

        else: check = True
        
        cont += 1
    return check


def data_mod(function): #Pede as informações do jogo a ser inserido ou alterado, verificando se as informações são válidas, e retorna as informações
    key = 1
    print("Insira a seguir as informações do jogo conforme informado. Caso queira cancelar o processo, digite 0 para o nome.")

    while (key == 1):
        name = input("Nome: ")
        gen = input("Gênero: ")
        price = (input("Preço com decimais: "))
        
        if(name == "0"):
            key = 0

        else:
            if(float_check(price) == None): 
                key = 1        
                print("Preço inválido, insira um número com decimais.")  
            else: 
                price = float_check(price)
                if(function == "insert"):
                    if(game_check(name) == False):
                        key = 1
                    else:
                        print(f"Nome escolhido: {name} Gênero escolhido: {gen} Preço escolhido: {price}")
                        confirm = input("Digite 1 para confirmar: ")
                        if(confirm == "1"): key = 0
                        else: key = 1
                else:
                    print(f"Nome escolhido: {name} Gênero escolhido: {gen} Preço escolhido: {price}")
                    confirm = input("Digite 1 para confirmar: ")
                    if(confirm == "1"): key = 0
                    else: key = 1

    return name, gen, price


#<-------------------------------------------------------------------------->
#<------------------------- COMANDOS DA BIBLIOTECA ------------------------->
#<-------------------------------------------------------------------------->


def viewall(): #Mostra as informações de todos os jogos
    data_prep()

    for linha in biblioteca: #Mostra todos os jogos
        print(" ".join(linha))
    return


def viewindv(): #Mostra as informações de um jogo específico, escolhendo o índice do jogo
    data_prep()

    cont = 0
    key = 1

    for linha in biblioteca: #Mostra o nome de todos os jogos
        print(f"Índice: {cont} Nome: {biblioteca[cont][0]}")
        cont+=1
    while (key == 1): #Verifica se o Índice é valido, se for mostra as informações do jogo escolhido
        view = int(input("Insira o índice de qual jogo você quer visualizar: "))
        if(view > (len(biblioteca) - 1)):
            print("Índice inválido.")
        else:
            print(" ".join(biblioteca[view]))
            key = 0
    return 


def insert(): #Insere um novo jogo no banco, pedindo as informações do jogo e escrevendo no banco
    data_prep()

    name, gen, price = data_mod("insert")
    
    if(name != "0"):
        with open("banco.csv", "a", encoding="utf-8") as banco:
            banco.write(f"{name},{gen},{price}\n") #Escreve as informações do jogo no banco
            banco.close()
        data_prep() #Atualiza a memória com as novas informações do banco

    else: print("Processo cancelado. Nenhum jogo foi inserido no banco.")
    return 


def delete(): #Deleta um jogo do banco, escolhendo o índice do jogo a ser deletado e reescrevendo o banco sem o jogo escolhido
    data_prep()
    cont = 0
    print("A seguir todos os jogos da biblioteca.")

    for linha in biblioteca: #Mostra o nome de todos os jogos
        print(f"Índice: {cont} {" ".join(linha)}")
        cont+=1

    view = int(input("Insira o índice do jogo que deseja deletar: ")) #Verifica o jogo que quer deletar
    if(view > (len(biblioteca) - 1)):
        print("Índice inválido.")

    else:
        print(" ".join(biblioteca[view]))
        confirm = input("Digite 1 para confirmar: ") #Confirma se deseja procedir

        if(confirm == "1"):
            del biblioteca[view] #Deleta o jogo escolhido da memória

            with open("banco.csv", "w", encoding="utf-8") as banco:
                banco.write("nome,genero,preco\n") #Reescreve o cabeçalho do banco
                for linha in biblioteca: #Reescreve o banco sem o jogo deletado
                    banco.write(",".join(linha)) 
                banco.close()
            data_prep() #Atualiza a memória com as novas informações do banco
        else: print("Processo cancelado. Nenhum jogo foi deletado do banco.")
    return 


def alter(): #Altera as informações de um jogo do banco, escolhendo o índice do jogo e reescrevendo o banco com as novas informações do jogo escolhido
    data_prep()

    cont = 0
    print("A seguir todos os jogos da biblioteca.")

    for linha in biblioteca: #Mostra o nome de todos os jogos
        print(f"Índice: {cont} {" ".join(linha)}")
        cont+=1

    view = int(input("Insira o índice do jogo que deseja alterar: "))
    if(view > (len(biblioteca) - 1)):
        print("Índice inválido.")

    else:
        print(" ".join(biblioteca[view]))
        confirm = input("Digite 1 para confirmar: ")

        if(confirm == "1"):
            name, gen, price = data_mod("alter")
            biblioteca[view] = [name, gen, f"{str(price)}\n"] #Atualiza as informações do jogo escolhido na memória
           
            with open("banco.csv", "w", encoding="utf-8") as banco:
                banco.write("nome,genero,preco\n") #Reescreve o cabeçalho do banco
                for linha in biblioteca:            #Reescreve o banco com o jogo alterado
                    banco.write(",".join(linha)) 
                banco.close()

            data_prep() #Atualiza a memória com as novas informações do banco
            print(biblioteca[view])

        else: print("Processo cancelado. Nenhum jogo foi alterado do banco.")
    return 