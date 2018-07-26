#import MySQLdb as mysql
import Configurations as Conf
import json

import pymysql as mysql

connection = mysql.connect(
    host = Conf.db_ip,
    user = Conf.user_db,
    passwd = Conf.user_db_password,
    db = Conf.db_schema,
    port = Conf.db_port)
cursor = connection.cursor()

fill_file = 'frases_keywords_train.json'

keywords_insert_string = """INSERT IGNORE INTO Keywords (keyword, orthography, type, cathegory)
VALUES ('{key}', '{orth}', '{type}', '{cathegory}')
ON DUPLICATE KEY UPDATE orthography='{orth}' , type='{type}' , cathegory='{cathegory}';"""

frases_insert_string = """INSERT IGNORE INTO Frases (frase, action)
VALUES ('{frase}', '{action}')
ON DUPLICATE KEY UPDATE action='{action}' ;"""

keyword_has_frases_string = """INSERT IGNORE INTO Keywords_has_Frases (keyword, frase)
VALUES ('{keyword}', '{frase}')
ON DUPLICATE KEY UPDATE keyword='{keyword}' , frase='{frase}';"""



try:
    with open(fill_file, "r") as infile:
        Tmp = json.load(infile)
        frases = Tmp["frases"]
        keywords = Tmp["keywords"]
        # Inserir na DB
        # Keywords
        for key in keywords:
            sql_command = str(keywords_insert_string).format(
                key=key,
                orth=keywords[key]['ORTH'],
                type=keywords[key]['TYPE'],
                cathegory=keywords[key]['CAT'])
            cursor.execute(sql_command)
        for frase in frases:
            sql_command = str(frases_insert_string).format(
                frase=frase,
                action=frases[frase]['action']
            )
            cursor.execute(sql_command)
            for keyword in frases[frase]['keywords']:
                sql_command = str(keyword_has_frases_string).format(
                    keyword=keyword,
                    frase=frase
                )
            cursor.execute(sql_command)

        connection.commit()
        cursor.close()
except FileNotFoundError:
    pass

class DB_Frases:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

class DB_Keywords:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
