import json
import os
from datetime import datetime

# Caminho do arquivo onde os dados dos clientes vão ser salvos
DATA_FILE = 'clientes.json'

# Função para carregar dados de clientes do arquivo
def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Função para salvar dados de clientes no arquivo
def salvar_dados(clientes):
    with open(DATA_FILE, 'w') as file:
        json.dump(clientes, file)

        # Função para criar um novo cliente
def novo_cliente(clientes):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    tipo_conta = input("Tipo de conta (comum/plus): ")
    saldo_inicial = float(input("Valor inicial da conta: "))
    senha = input("Senha: ")

    # Validação do tipo de conta
    if tipo_conta not in ['comum', 'plus']:
        print("Tipo de conta inválido!")
        return

    # Criação do cliente
    clientes[cpf] = {
        'nome': nome,
        'tipo_conta': tipo_conta,
        'saldo': saldo_inicial,
        'senha': senha,
        'extrato': [],
    }

    salvar_dados(clientes)
    print("Cliente criado com sucesso!")

# Função para apagar um cliente
def apaga_cliente(clientes):
    cpf = input("Informe o CPF do cliente a ser apagado: ")
    if cpf in clientes:
        del clientes[cpf]
        salvar_dados(clientes)
        print("Cliente apagado com sucesso!")
    else:
        print("Cliente não encontrado!")

# Função para debitar um valor da conta do cliente
def debito(clientes):
    cpf = input("CPF: ")
    senha = input("Senha: ")
    valor = float(input("Valor a debitar: "))

    cliente = clientes.get(cpf)
    if cliente and cliente['senha'] == senha:
        taxa = 0.05 if cliente['tipo_conta'] == 'comum' else 0.03
        total_debito = valor + (valor * taxa)

        # Verifica se o débito é permitido
        if cliente['saldo'] - total_debito >= (-1000 if cliente['tipo_conta'] == 'comum' else -5000):
            cliente['saldo'] -= total_debito
            cliente['extrato'].append({'data': str(datetime.now()), 'tipo': 'debito', 'valor': total_debito})
            salvar_dados(clientes)
            print("Débito realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o débito!")
    else:
        print("CPF ou senha inválidos!")

# Função para depositar um valor na conta do cliente
def deposito(clientes):
    cpf = input("CPF: ")
    valor = float(input("Valor a depositar: "))

    if cpf in clientes:
        clientes[cpf]['saldo'] += valor
        clientes[cpf]['extrato'].append({'data': str(datetime.now()), 'tipo': 'deposito', 'valor': valor})
        salvar_dados(clientes)
        print("Depósito realizado com sucesso!")
    else:
        print("Cliente não encontrado!")

# Função para exibir o extrato do cliente
def extrato(clientes):
    cpf = input("CPF: ")
    senha = input("Senha: ")

    cliente = clientes.get(cpf)
    if cliente and cliente['senha'] == senha:
        print(f"Extrato de {cliente['nome']}:")
        for movimento in cliente['extrato']:
            print(f"{movimento['data']} - {movimento['tipo'].capitalize()}: R$ {movimento['valor']:.2f}")
        print(f"Saldo atual: R$ {cliente['saldo']:.2f}")
    else:
        print("CPF ou senha inválidos!")

# Função para transferir valores entre contas
def transferencia(clientes):
    cpf_origem = input("CPF (Origem): ")
    senha_origem = input("Senha (Origem): ")
    cpf_destino = input("CPF (Destino): ")
    valor = float(input("Valor a transferir: "))

    cliente_origem = clientes.get(cpf_origem)
    cliente_destino = clientes.get(cpf_destino)

    if cliente_origem and cliente_origem['senha'] == senha_origem and cliente_destino:
        taxa = 0.05 if cliente_origem['tipo_conta'] == 'comum' else 0.03
        total_debito = valor + (valor * taxa)

        # Verifica se a transferência é permitida
        if cliente_origem['saldo'] - total_debito >= (-1000 if cliente_origem['tipo_conta'] == 'comum' else -5000):
            cliente_origem['saldo'] -= total_debito
            cliente_destino['saldo'] += valor
            cliente_origem['extrato'].append({'data': str(datetime.now()), 'tipo': 'transferencia', 'valor': total_debito})
            cliente_destino['extrato'].append({'data': str(datetime.now()), 'tipo': 'recebido', 'valor': valor})
            salvar_dados(clientes)
            print("Transferência realizada com sucesso!")
        else:
            print("Saldo insuficiente para realizar a transferência!")
    else:
        print("CPF ou senha inválidos!")

# Função para exibir dados do usuário
def dados_usuario(clientes):
    cpf = input("CPF: ")
    senha = input("Senha: ")

    cliente = clientes.get(cpf)
    if cliente and cliente['senha'] == senha:
        print(f"Nome: {cliente['nome']}")
        print(f"Tipo de Conta: {cliente['tipo_conta']}")
        print(f"Saldo: R$ {cliente['saldo']:.2f}")
    else:
        print("CPF ou senha inválidos!")

# Função principal que mantém o menu
def main():
    clientes = carregar_dados()
    
    while True:
        print("\nMenu:")
        print("1 - Novo Cliente")
        print("2 - Apagar Cliente")
        print("3 - Débito")
        print("4 - Depósito")
        print("5 - Extrato")
        print("6 - Transferência")
        print("7 - Seus Dados")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            novo_cliente(clientes)
        elif opcao == '2':
            apaga_cliente(clientes)
        elif opcao == '3':
            debito(clientes)
        elif opcao == '4':
            deposito(clientes)
        elif opcao == '5':
            extrato(clientes)
        elif opcao == '6':
            transferencia(clientes)
        elif opcao == '7':
            dados_usuario(clientes)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
