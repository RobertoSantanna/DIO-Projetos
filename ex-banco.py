# Dicionário para armazenar os dados dos clientes
clientes = {}

# Função para realizar depósito
def deposito(conta, valor):
    if conta in clientes:
        clientes[conta][1] += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Conta não encontrada.")

# Função para realizar saque
def saque(conta, valor):
    if conta in clientes:
        if clientes[conta][1] >= valor:
            clientes[conta][1] -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")

# Função para exibir extrato
def extrato(conta):
    if conta in clientes:
        print("Nome do Cliente:", clientes[conta][0])
        print("Saldo da Conta:", clientes[conta][1])
    else:
        print("Conta não encontrada.")

# Loop principal do sistema
while True:
    print("===== Banco Python =====")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor do depósito: "))
        deposito(conta, valor)
    elif opcao == "2":
        conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor do saque: "))
        saque(conta, valor)
    elif opcao == "3":
        conta = input("Digite o número da conta: ")
        extrato(conta)
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")