
import re


def CriarContaCorrente(_lista_contas_corrente):

    _nova_conta = {}

    _nova_conta["agencia"] = str("0001")
    _nova_conta["numero_conta"] = int(input("Digite o numero da Nova Conta: "))

    if _lista_contas_corrente == []:
        
        _nova_conta["cpf"] = str(input("Digite o CPF: "))
        _nova_conta["cpf"] = re.sub('[^0-9]', '', _nova_conta["cpf"])

        return _nova_conta
    
    else:
        for _conta in _lista_contas_corrente:

            if _conta.get("numero_conta") == _nova_conta.get("numero_conta"):

                return 0

            else:

                _nova_conta["cpf"] = str(input("Digite o CPF: "))
                _nova_conta["cpf"] = re.sub('[^0-9]', '', _nova_conta["cpf"])

            return _nova_conta

def CriarUsuario(_usuarios_cadastrados):

    _usuario = {}

    _usuario["cpf"] = str(input("Digite o CPF: "))
    _usuario["cpf"] = re.sub('[^0-9]', '', _usuario["cpf"])

    if _usuario["cpf"] in _usuarios_cadastrados:

        return 0

    else:

        _usuario["nome"] = str(input("Digite o nome do usuario: "))
        _usuario["data_nascimento"] = str(input("Digite a data de nascimento (mes/dia/ano): "))

        _logradouro = str(input("Digite o nome da rua: ")) + ", "
        _numero = str(input("Digite o numero: ")) + " - "
        _bairro = str(input("Digite o bairro: ")) + " - "
        _cidade = str(input("Digite a cidade: ")) + "/"
        _uf = str(input("Digite o UF do Estado: "))

        endereco = f"{_logradouro}{_numero}{_bairro}{_cidade}{_uf}"

        _usuario["endereco"] = endereco

        return _usuario

def Extrato(_saldo, _extrato):
    print("=" * 20)
    print("Extrato Detalhado".center(20))
    print("=" * 20)
    print(f"Saldo: {_saldo}\n")
    print("Sem movimentações recentes" if _extrato == "" else _extrato)
    
def Sacar(_saldo, _numero_saques, _extrato, _LIMITE_SAQUES):

    _saque = int(input("Digite o valor a ser Sacado R$: "))
        
    if _numero_saques == _LIMITE_SAQUES:
        print("Não foi possivel realizar a operação, Limite de Saques atingido.")
        return _saldo, _numero_saques, _extrato

    elif _saque > _saldo:
        print("Não foi possivel realizar a operação, Saldo insuficiente.")
        return _saldo, _numero_saques, _extrato
        
    elif _saque > 500:
        print("Não foi possivel realizar a operação, Saque acima do valor permitido.")
        return _saldo, _numero_saques, _extrato
        
    else:
        _saldo -= _saque
        _numero_saques += 1
        _extrato += f"Saque: R$ {_saque:.2f}\n"

        print("Saque realizado com sucesso!")

        return _saldo, _numero_saques, _extrato

def Depositar(_saldo, _extrato):

    _deposito = int(input("Digite o valor a ser depositado R$: "))

    if _deposito <= 0:
        print("\nNão é possivel depositar um valor negativo ou nulo!\n")
        
    else:
        _saldo += _deposito
        _extrato += f"Depósito: R$ {_deposito:.2f}\n"

        print("Depósito de realizado com sucesso!")

        return _saldo, _extrato


menu = """

[u] Novo Usuario
[c] Nova Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

lista_usuarios = usuarios_cadastrados = lista_contas_corrente =  []
saldo = numero_saques = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)

    if opcao == "c":
        nova_conta = CriarContaCorrente(lista_contas_corrente)

        if nova_conta == 0:
            print("Erro: Conta já cadastrada anteriormente.")
        else:
            lista_contas_corrente.append(nova_conta)

    elif opcao == "u":

        novo_usuario = CriarUsuario(usuarios_cadastrados)

        if novo_usuario == 0:

            print("Usuario já castrado")
        
        else:

            usuarios_cadastrados.append(novo_usuario['cpf'])
            lista_usuarios.append(novo_usuario)

    elif opcao == "d":

        saldo, extrato = Depositar(saldo, extrato)

    elif opcao == "s":

        saldo, numero_saques, extrato = Sacar(_saldo = saldo, _extrato = extrato, _numero_saques = numero_saques, _LIMITE_SAQUES = LIMITE_SAQUES)

    elif opcao == "e":
        
        Extrato(saldo, _extrato = extrato)

    elif opcao == "q":
        break

    else:
        print("Opção Inválida!")
