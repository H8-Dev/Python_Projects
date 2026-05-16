# Campo para chamada de módulos
import funcoes

def menu():
    while True:
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
                input("v Pressione Enter para voltar ao menu...")
            case "2":
                funcoes.viewindv()
                input("v Pressione Enter para voltar ao menu...")
            case "3":
                funcoes.insert()
                input("v Pressione Enter para voltar ao menu...")
            case "4":
                funcoes.delete()
                input("v Pressione Enter para voltar ao menu...")
            case "5":
                funcoes.alter()
                input("v Pressione Enter para voltar ao menu...")
            case "0":
                break
            case _:
                print("<            Valor Inválido!!         >")
                input("v Pressione Enter para voltar ao menu...")

if __name__ == "__main__":
    menu()