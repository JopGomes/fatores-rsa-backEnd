import mysql.connector
from mysql.connector import Error

class BancoDados:
    def __init__(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="pontes",
                passwd="abacate123",
                database="dbVE2"
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    def inserirNumero(self,primo1, primo2):    
        cursor = self.connection.cursor()
        query = "INSERT INTO fatorDePrimos VALUES (" + str(primo1*primo2) + "," + str(primo1) + "," + str(primo2) + ")"
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def buscarFatores(self,n):
        query = "select fator1,fator2 from fatorDePrimos WHERE produto ="+str(n)
        cursor = self.connection.cursor()
        cursor.execute(query)
        resultado = cursor.fetchone()
        if resultado:
            print(resultado)
            return resultado
        else:
            print("Não é fator de dois primos")
            return False
    
    def apagarTuplas(self):
        query = "Delete from fatorDePrimos"
        cursor = self.connection.cursor()
        cursor.execute(query)