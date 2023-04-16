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
        
def cadastrar_usuario(clientes, nome, cpf):
    cliente = {"nome": nome, "cpf": cpf, "contas": []}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

# Função para cadastrar uma nova conta bancária para um cliente
def cadastrar_conta_bancaria(clientes, cpf, conta, saldo):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            conta_bancaria = {"conta": conta, "saldo": saldo}
            cliente["contas"].append(conta_bancaria)
            print("Conta bancária cadastrada com sucesso!")
            return
    print("Cliente não encontrado.")

# Função para realizar um saque em uma conta bancária
def realizar_saque(clientes, cpf, conta, valor):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            for conta_bancaria in cliente["contas"]:
                if conta_bancaria["conta"] == conta:
                    if conta_bancaria["saldo"] >= valor:
                        conta_bancaria["saldo"] -= valor
                        print("Saque realizado com sucesso!")
                        return
                    else:
                        print("Saldo insuficiente.")
                        return
            print("Conta bancária não encontrada.")
            return
    print("Cliente não encontrado.")

# Função para realizar um depósito em uma conta bancária
def realizar_deposito(clientes, cpf, conta, valor):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            for conta_bancaria in cliente["contas"]:
                if conta_bancaria["conta"] == conta:
                    conta_bancaria["saldo"] += valor
                    print("Depósito realizado com sucesso!")
                    return
            print("Conta bancária não encontrada.")
            return
    print("Cliente não encontrado.")

# Função para obter o extrato de uma conta bancária
def obter_extrato(clientes, cpf, conta):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            for conta_bancaria in cliente["contas"]:
                if conta_bancaria["conta"] == conta:
                    print("Extrato:")
                    print("Conta:", conta_bancaria["conta"])
                    print("Saldo:", conta_bancaria["saldo"])
                    return
            print("Conta bancária não encontrada.")
            return
    print("Cliente não encontrado.")

# Exemplo de uso das funções
clientes = []

# Cadastrar um novo cliente
cadastrar_usuario(clientes, "João", "12345678901")

# Cadastrar uma nova conta bancária para o cliente
cadastrar_conta_bancaria(clientes, "12345678901", "001", 1000.0)

# Realizar um saque na conta bancária do cliente
realizar_saque(clientes, "12345678901", "001", 500.0)

# Realizar um depósito na conta bancária do cliente
realizar_deposito(clientes, "12345678901", "001", 200.0)

# Obter o extrato da conta bancária do cliente
obter_extrato(clientes, "12345678901", "001")