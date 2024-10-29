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
