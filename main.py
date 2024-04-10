def Saque(_saldo, _limite_saque):

    saque = float(input("Qual o valor a ser sacado ?: "))

    while True:

        if saque > _saldo:
            print("Não foi possivel realizar o saque. Saldo insuficiente\n")
            break

        elif _limite_saque <= 0:
            print("Não foi possivel realizar o saque. Limite de saque diario atingido.")
            break

        else:
            _saldo -= saque
            _limite_saque -= 1

            return _saldo, _limite_saque


def Deposito(_saldo):
    
    deposito = 0

    while True:
        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito <= 0:
            print("\nNão é possivel depositar valores negativos ou nulo.\n")

        else:
            print(f"\nO valor de R$ {deposito:.2f} foi depositado com sucesso!")
            _saldo += deposito

            return _saldo, deposito
            


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = ultimo_deposito = 0
limite = 500
limite_saques = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        saldo, ultimo_deposito = Deposito(saldo)

    elif opcao == "s":
        saldo, limite_saques = Saque(saldo, limite_saques)

    elif opcao == "e":
        extrato = f""" Saldo R$ {saldo:.2f}\n Ultimo Depósito R$ {ultimo_deposito:.2f}"""
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Opção Inválida!")
