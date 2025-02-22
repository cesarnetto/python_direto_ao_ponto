import os
import csv

def salvar_csv (dicionario, cabecalho, arquivo):
    """Salva o dicionário em um arquivo CSV."""
    with open (arquivo, 'w', newline='') as file:
        writer = csv.DictWriter (file, fieldnames=cabecalho)
        writer.writeheader()
        writer.writerows(dicionario)

def ler_csv(arquivo):
    """Lê o arquivo CSV e retorna uma lista de dicionários."""
    lista = []
    try:
        with open (arquivo, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                lista.append(dict(row))
    except FileExistsError:
        print(f"{arquivo} não encontrado.")
        print("Um novo arquivo será gerado.")
    return lista

def exibir_cadastrados(pessoas):
    """Exibe os dados registrados formatados."""
    print(f"\nNome\tEmail")
    for pessoa in pessoas:
        nome = pessoa['nome']
        email = pessoa['email']
        print(f"{nome}\t{email}")

def adicionar_registro(nome, email, lista):
    """Adiciona uma nova pessoa á lista"""
    d = {'nome': nome, 'email': email}
    lista.append(d)
    return lista

def menu():
    print("Cadastro de usuários")
    print("====================\n")
    print("Opções:")
    print("1. Adicionar novo registro")
    print("2. Exibir registros")
    print("3. Sair\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    arquivo = "cadastro.csv"
    pessoas = ler_csv(arquivo)
    cabecalho = ['nome', 'email']

    while True:
        limpar_tela()
        menu()
        opcao = input("Selecione uma opção: ").strip ()
        if opcao == "1":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()

            if not nome or not email:
                print("Por favor, ", end="")
                print("insira um nome e um email válidos.")
                continue

            pessoas = adicionar_registro(nome, email, pessoas)
            print("\nRegistro adicionado com sucesso")

        elif opcao == "2":
            if pessoas:
                exibir_cadastrados(pessoas)
            else:
                print("Nenhum registro encontrado.")
        
        elif opcao == "3":
            print("Saindo...")
            salvar_csv(pessoas, cabecalho, arquivo)
            break

        else:
            print("Opção inválida.")
            print("Escolha uma opção entre 1, 2 e 3.")
        input("\nAperte Enter para continuar")
        
if __name__ == "__main__":
    main()