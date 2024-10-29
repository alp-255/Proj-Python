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
