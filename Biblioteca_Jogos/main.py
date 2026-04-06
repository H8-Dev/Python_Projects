# Campo para chamada de módulos
import funcoes

key = 1 # Chave pra fazer o menu rodar

while(key == 1):
    print("<  Bem Vindo a Bibliotecar de Jogos!  >\n" \
        "<                Opções               >\n" \
        "<      Visualizar Todos Jogos (1)     >\n" \
        "<         Visualizar Um Jogo (2)      >\n" \
        "<           Inserir Jogos (3)         >\n" \
        "<           Deletar Jogos (4)         >\n" \
        "<           Alterar Jogos (5)         >\n" \
        "<                Sair (0)             >")
    entrada = (input("^       Insira a opção desejada: "))
    
    match entrada:
        case "1":
            funcoes.viewall()
            useless = input("v Pressione Enter para voltar ao menu...")
        case "2":
            funcoes.viewindv()
            useless = input("v Pressione Enter para voltar ao menu...")
        case "3":
            funcoes.insert()
            useless = input("v Pressione Enter para voltar ao menu...")
        case "4":
            funcoes.delete()
            useless = input("v Pressione Enter para voltar ao menu...")
        case "5":
            funcoes.alter()
            useless = input("v Pressione Enter para voltar ao menu...")
        case "0":
            key = 0
        case _:
            print("<            Valor Inválido!!         >")
            useless = input("v Pressione Enter para voltar ao menu...")