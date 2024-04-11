def Depositar(_saldo, _extrato):

    deposito = int(input("Digite o valor a ser depositado R$: "))

    if deposito <= 0:
        print("\nNão é possivel depositar um valor negativo ou nulo!\n")
        
    else:
        _saldo += deposito
        _extrato += f"Depósito: R$ {deposito:.2f}\n"

        return _saldo, _extrato


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = numero_saques = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":

        saldo, extrato = Depositar(saldo, extrato)

        print("Depósito realizado com sucesso!")

    elif opcao == "s":

        saque = int(input("Digite o valor a ser Sacado R$: "))
        
        if numero_saques == LIMITE_SAQUES:
            print("Não foi possivel realizar a operação, Limite de Saques atingido.")

        elif saque > saldo:
            print("Não foi possivel realizar a operação, Saldo insuficiente.")
        
        elif saque > 500:
            print("Não foi possivel realizar a operação, Saque acima do valor permitido.")
        
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"

            print("Saque realizado com sucesso!")


    elif opcao == "e":
        print("=" * 20)
        print("Extrato Detalhado".center(20))
        print("=" * 20)
        print(f"Saldo: {saldo}\n")
        print("Sem movimentações recentes" if extrato == "" else extrato)

    elif opcao == "q":
        print()
        break

    else:
        print("Opção Inválida!")
