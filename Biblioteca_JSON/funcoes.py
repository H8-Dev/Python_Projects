# Entrada das bibliotecas
import json

# Variavel global essencial.
biblioteca = []

#<-------------------------------------------------------------------------->
#<------------------------- COMANDOS DE PREPARAÇÃO ------------------------->
#<-------------------------------------------------------------------------->

def data_prep():
    global biblioteca
    biblioteca.clear() #Limpa a memória para evitar repetições
    with open("banco.json", "r", encoding="utf-8") as banco:
        biblioteca = json.load(banco)
    return


def float_check(price): #Verifica se o valor inserido é um número decimal, caso contrário pede para inserir novamente
    try:
        float(price)
        return round(float(price), 2)
    except ValueError:
        return None


def game_check(name): #Verifica se o nome do jogo já existe no banco, caso exista invalida o insert
    for item in biblioteca:

        if(name == item["nome"]):
            print("Jogo já existe no banco. Insira um jogo válido")
            check = False
            break

        else: check = True
        

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

    for item in biblioteca:
        print(f"Nome: {item['nome']} Gênero: {item['genero']} Preço: {item['preço']}\n")
    return

def viewindv(): #Mostra as informações de um jogo específico, escolhendo o índice do jogo
    data_prep()

    for item in biblioteca:
        print(f"Índice: {biblioteca.index(item)} Nome: {item['nome']}")
    
    while True:
        try:
            view = int(input("Insira o índice de qual jogo você quer visualizar: "))
            if(view > (len(biblioteca) -1)):
                print("Índice inválido.")
            else:
                print(f"Nome: {biblioteca[view]['nome']} Gênero: {biblioteca[view]['genero']} Preço: {biblioteca[view]['preço']}\n")
                break
        except ValueError:
            print("Valor inválido. Insira um dos índices listados.")
    return

def insert(): #Insere um novo jogo no banco, pedindo as informações do jogo e escrevendo no banco
    data_prep()

    name, gen, price = data_mod("insert")

    if(name != "0"):
        novo_jogo = {
            "nome": name,
            "genero": gen,
            "preço": price
        }
        biblioteca.append(novo_jogo)
        with open("banco.json", "w", encoding="utf-8") as banco:
            json.dump(biblioteca, banco, indent=4, ensure_ascii=False)
    return

def delete(): #Deleta um jogo do banco, escolhendo o índice do jogo a ser deletado e reescrevendo o banco sem o jogo escolhido
    data_prep()
    
    for item in biblioteca:
        print(f"Índice: {biblioteca.index(item)} Nome: {item['nome']}")

    while True:
        try:
            view = int(input("Insira o índice de qual jogo você quer deletar: "))
            if(view > (len(biblioteca) -1)):
                print("Índice inválido.")
            else:
                print(f"Nome: {biblioteca[view]['nome']} Gênero: {biblioteca[view]['genero']} Preço: {biblioteca[view]['preço']}\n")
                break
        except ValueError:
            print("Valor inválido. Insira um dos índices listados.")

    confirm = input("Digite 1 para confirmar: ")
    if(confirm == "1"):
        del biblioteca[view]
        with open("banco.json", "w", encoding="utf-8") as banco:
            json.dump(biblioteca, banco, indent=4, ensure_ascii=False)
    else:
        print("Processo cancelado. Nenhum jogo foi deletado da biblioteca.")

    return

def alter(): #Altera as informações de um jogo do banco, escolhendo o índice do jogo e reescrevendo o banco com as novas informações do jogo escolhido
    data_prep()
    for item in biblioteca:
        print(f"Índice: {biblioteca.index(item)} Nome: {item['nome']}")
        
    while True:
        try:
            view = int(input("Insira o índice de qual jogo você quer alterar: "))
            if(view > (len(biblioteca) -1)):
                print("Índice inválido.")
            else:
                print(f"Nome: {biblioteca[view]['nome']} Gênero: {biblioteca[view]['genero']} Preço: {biblioteca[view]['preço']}\n")
                break
        except ValueError:
            print("Valor inválido. Insira um dos índices listados.")

    confirm = input("Digite 1 para confirmar: ")
    if(confirm == "1"):
        name, gen, price = data_mod("alter")
        if(name != "0"):
            biblioteca[view] = {
                "nome": name,
                "genero": gen,
                "preço": price
            }
            with open("banco.json", "w", encoding="utf-8") as banco:
                json.dump(biblioteca, banco, indent=4, ensure_ascii=False)
    else:
        print("Processo cancelado. Nenhum jogo foi alterado da biblioteca.")

    return