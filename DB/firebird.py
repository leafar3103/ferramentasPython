import fdb

# Use barras invertidas duplas
database_path = r'C:\Otica\Arquivos\Otica.gdb'

# OU use uma barra invertida crua
# database_path = r'C:\Otica\Arquivos\Otica.gdb'

# Restante do código...
try:
    conn = fdb.connect(
        dsn=database_path,
        user='SYSDBA',
        password='masterey'
    )
    print("Conexão bem-sucedida!")

    # Realize operações no banco de dados, se necessário

    # Feche a conexão quando terminar
    conn.close()

except fdb.Error as e:
    print(f"Erro durante a conexão: {e}")
