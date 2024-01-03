import fdb
from tkinter.filedialog import askdirectory

# Use barras invertidas duplas
database_path = askdirectory(title="Pasta Origem")

# OU use uma barra invertida crua
# database_path = askdirectory(title="Pasta Origem")

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
