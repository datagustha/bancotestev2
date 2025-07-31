# Connects to a SQL database using pyodbc

# importando bibioteca

import mysql.connector
from mysql.connector import errorcode
import pandas as pd

valor = 1

while True:

    valor = int(input("digite um valor "))
    print(type(valor))

    if valor == 0:
        print(" senha correta!")

        try:
            mydb = mysql.connector.connect(
                host="192.168.100.200",
                user="simfacilita",
                password="NVjv*Ae2GPQ01.AK",
                database="dbsimfacilita",
            )
            print("conexao bem sucedida! ✅")

        except mysql.connector.Error as error:
            print("não foi possivel conectar")

    else:
        print("senha incorreta tente novamente! ")

# consultar banco dados
cursor = mydb.cursor()


db = pd.read_sql(
    """
select * from fpgtoSemearBoleto order by dtpgto desc , cliente desc limit 10
""",
    con=mydb,
)

# expandir consulta
# pd.set_option("max_columns", None)

# colunas do df
print(f"\n colunas = {list(db.columns)}\n")

# mostrar todas no db
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# selecionar colunas

colunas = ["cliente", "contrato", "dtPgto"]

db = db[colunas]

print(db)
