import os

def ler_anotacoes_do_arquivo(nome_do_arquivo):
    try:
        with open (nome_do_arquivo, 'r') as arquivo:
            anotacoes = arquivo.readlines()
            # Remove os \n com um list comprehension
            anotacoes = [anotacoes.rstrip()
                         for anotacao in anotacoes]
            return anotacoes
    except FileNotFoundError:
        return []

def salvar_anotacoes_no_arquivo (nome_do_arquivo, anotacoes):
    with open(nome_do_arquivo, 'w') as file:
        # Adiciona os \n para salvar uma anotação por linha
        notes = [anotacao+'\n' for anotacao in anotacoes]
        file.writelines(notes)

def exibir_anotacao(anotacao):
    tamanho_anotacao = len (anotacao) + 6
    print('-' * tamanho_anotacao)
    print(' ' * 3, anotacao)
    print('-' * tamanho_anotacao)
    print()

def exibir_todas_anotacoes(anotacoes):
    print("\n" + "Anotações".center(30, "="))
    for anotacao in anotacoes:
        exibir_anotacao(anotacao)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def executar():
    nome_do_arquivo = "anotacoes.txt"
    anotacoes = ler_anotacoes_do_arquivo(nome_do_arquivo)

    while True:
        limpar_tela()
        print("TODO APP")
        print("=========\n")
        print("1. Adicionar nota")
        print("2. Ver anotações")
        print("3. Sair\n")

        acao = input("Insira sua opção: ")

        if acao == '1':
            anotacao = input("Anotação: ")
            anotacoes.append (anotacao)
            exibir_todas_anotacoes (anotacoes)
        
        elif acao == '2':
            exibir_todas_anotacoes (anotacoes)
        
        elif acao == '3':
            salvar_anotacoes_no_arquivo(nome_do_arquivo, anotacoes)
            break
        else:
            print("Opção inválida.", end="")
            print("Por favor, tente novamente.")
        input("\nAperte Enter para continuar")

if __name__ == "__main__":
    executar()        
