import fdb
from tkinter.filedialog import askdirectory
# import pandas as pd

# Substitua os valores com as configurações do seu banco de dados
host= 'localhost'
database_path=askdirectory(title="Pasta Origem")
user='SYSDBA'
password='masterkey'

# Criar a conexão
try:    
    conn = fdb.connect(
    host=host,
    database=database_path,
    user=user,
    password=password
    )
    print("Conexão bem-sucedida!")
    cur=conn.cursor()
    cur.execute("SELECT * FROM ")
    rows = cur.fetchall()

    # Processar os resultados
    for row in rows:
        print(row)

    conn.close()
except fdb.Error as e:
    print(f"Erro durante a conexão: {e}")
# Exemplo de consulta SQL
# Usar o Pandas para executar a consulta
# df = pd.read_sql_query(sql_query, conn)

# Exibir o DataFrame
# print(df)

# Fechar a conexão após a conclusão
