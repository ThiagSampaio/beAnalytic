import requests
import pandas as pd
import mysql.connector
from mysql.connector import Error

# ---- Puxando infos da api --------------
def getInfo1():
    'Pega as infos para tabela jogo '
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    response = requests.get(url)
    response_json = response.json()
    new_data = response_json['applist']['apps']['app']
    teste = pd.json_normalize(new_data)
    
    return teste




# ----- Operaçoes DB 

def quantidade_info():
    'Funcao para ver se existe dado no DB'

    try:
        con = mysql.connector.connect(host='localhost',database='beanalytic',user='root',password='e2h8Ta6i9qnUPt')
        consulta_sql = "select * from jogo"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        #print("Número total de registros retornados: ", cursor.rowcount)
        if cursor.rowcount > 0 :
            if (con.is_connected()):
                con.close()
                cursor.close()
                #print("Conexão ao MySQL encerrada")
            return True
        else:
            if (con.is_connected()):
                con.close()
                cursor.close()
                #print("Conexão ao MySQL encerrada")
            return False

    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()
            print("Conexão ao MySQL encerrada")

teste = quantidade_info()
print(teste)

