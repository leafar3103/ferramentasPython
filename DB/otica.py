import pandas as pd
from tkinter.filedialog import askdirectory

# Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo Excel
caminho_arquivo = askdirectory(title="Pasta Origem")

# Carregar o arquivo Excel para um DataFrame do Pandas
dados = pd.read_excel(caminho_arquivo)
# Escolha a coluna específica (substitua 'nome_da_coluna' pelo nome real da coluna)
print(dados)
nome_da_coluna = 'Unnamed: 7'

# Exibir todas as linhas da coluna específica
coluna_selecionada = dados.iloc[1, :]

# Exibir a coluna selecionada
print(coluna_selecionada)

# # Exibir todos os dados
#
# # Iterar sobre as colunas e exibir cada uma
# for coluna in dados.columns:
#     # Filtrar os valores NaN na coluna
#     valores_sem_nan = dados[coluna].dropna()
    
#     # Exibir o nome da coluna
#     print(f"Coluna: {coluna}")
    
#     # Exibir os valores sem NaN na coluna
#     print(valores_sem_nan)
    
#     # Adicionar uma linha em branco para separar as colunas
#     print("\n" + "="*30 + "\n")