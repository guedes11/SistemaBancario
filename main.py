def Extrato(_saldo, _extrato):
    print("=" * 20)
    print("Extrato Detalhado".center(20))
    print("=" * 20)
    print(f"Saldo: {_saldo}\n")
    print("Sem movimentações recentes" if _extrato == "" else _extrato)
    

def Sacar(_saldo, _numero_saques, _extrato, _LIMITE_SAQUES):

    saque = int(input("Digite o valor a ser Sacado R$: "))
        
    if _numero_saques == _LIMITE_SAQUES:
        print("Não foi possivel realizar a operação, Limite de Saques atingido.")
        return _saldo, _numero_saques, _extrato

    elif saque > _saldo:
        print("Não foi possivel realizar a operação, Saldo insuficiente.")
        return _saldo, _numero_saques, _extrato
        
    elif saque > 500:
        print("Não foi possivel realizar a operação, Saque acima do valor permitido.")
        return _saldo, _numero_saques, _extrato
        
    else:
        _saldo -= saque
        _numero_saques += 1
        _extrato += f"Saque: R$ {saque:.2f}\n"

        print("Saque realizado com sucesso!")

        return _saldo, _numero_saques, _extrato

def Depositar(_saldo, _extrato):

    deposito = int(input("Digite o valor a ser depositado R$: "))

    if deposito <= 0:
        print("\nNão é possivel depositar um valor negativo ou nulo!\n")
        
    else:
        _saldo += deposito
        _extrato += f"Depósito: R$ {deposito:.2f}\n"

        print("Depósito de realizado com sucesso!")

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

    elif opcao == "s":

        saldo, numero_saques, extrato = Sacar(_saldo = saldo, _extrato = extrato, _numero_saques = numero_saques, _LIMITE_SAQUES = LIMITE_SAQUES)

    elif opcao == "e":
        
        Extrato(saldo, _extrato = extrato)

    elif opcao == "q":
        break

    else:
        print("Opção Inválida!")
