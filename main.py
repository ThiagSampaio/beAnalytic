import requests
import pandas as pd
import mysql.connector
from mysql.connector import Error
import pymysql



# ---- Puxando infos da api --------------
def getInfo1():
    'Pega as infos para tabela jogo '
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    response = requests.get(url)
    response_json = response.json()
    new_data = response_json['applist']['apps']['app']
    teste = pd.json_normalize(new_data)
    
    return teste
def getInfo2():
    'Pega as infos para tabela jogo '
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    response = requests.get(url)
    response_json = response.json()
    new_data = response_json['applist']['apps']['app']
    teste = pd.json_normalize(new_data)
    
    return teste

# ---- Joga os dados na tabela -------

def putDados1():    
    try:
        dataframe = getInfo1()
        db = mysql.connector.connect(host='localhost',database='beanalytic',user='root',password='e2h8Ta6i9qnUPt')
        if(db):
            print('Conect')
        else:
            print('falha')
        cur = db.cursor()
        cur.execute('DELETE from jogo')

        query = db.cursor()

        for(row, rs) in dataframe.iterrows():
            appid = rs[0]
            name = rs[1]
            syntext = """INSERT INTO jogo (appid, name) VALUES (%s,%s)"""
            value = (appid,name)
            query.execute(syntext,value)
            db.commit()

    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
    finally:
        if (db.is_connected()):
                db.close()
                db.close()
                print("Conexão ao MySQL encerrada")
    
putDados1()

