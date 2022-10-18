
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Você não tem saldo suficiente.")

    elif valor > limite:
        print("O valor do saque excede o limite.")

    elif numero_saques >= limite_saques:
        print("Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("O valor informado é inválido.")

    return saldo, extrato

def mostrar_extrato(sakdo, /, *, extrato ):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário cadastrado com esse CPF")
        return
    
    nome = input("Digite o Nome: ")
    data_nascimento = input("Digite a data de Nascimento: ")
    endereco = input("Digite o Endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def buscar_usuario(cpf, usuarios):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_encontrado[0] if usuario_encontrado else None

def criar_conta(agencia, conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "conta": conta, "usuario": usuario}
    
    print("Usuário não cadastrado! ")

def listar_contas(contas):
    for conta in contas:
        print (f'''
            Agência: {conta['agencia']:}
            Conta: {conta['conta']:}
            Titular: {conta['usuario']['nome']:}
        ''')

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Novo Usuário
[6] Listar Contas
[7] Sair
=> """   

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)      

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES,
        )
        
    elif opcao == "3":
        mostrar_extrato(saldo, extrato = extrato)

    elif opcao == "4":
        conta = len(contas) + 1
        criar_conta(AGENCIA, conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "5": 
        criar_usuario(usuarios)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "7":
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida!")