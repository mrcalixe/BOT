# -*- coding: utf-8 -*-

import random
import sqlite3 as sql
# import pymongo as mongo

def oneOf(arr):
    rand_idx = random.randint(0,len(arr) - 1)
    return arr[rand_idx]

class State:
    def __init__(self):
        self.sys = 1

class Knowledge_BD:
    def __init__(self, tables = False):
        self.db = sql.connect('knowledge/db')
        self.id = 0
        if tables:
            cursor = self.db.cursor()
            cursor.execute('''
                CREATE TABLE music(id INTEGER PRIMARY KEY,\
                                   author TEXT,
                                   band TEXT,
                                   year INTEGER,
                                   music TEXT)
                                ''')
            self.db.commit()
            cursor.close()

    def insert_knowledge(self, author, band, year, music):
        cursor = self.db.cursor()
        cursor.execute('''
            INSERT INTO music(id, author, band, year, music)
            VALUES (?,?,?,?,?), (self.id, author, band, year, music)''')
        self.db.commit()
        cursor.close()

    def get_by_author(self, author):
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT * FROM music
              WHERE author = ?''', author)
        all_rows = self.cursor.fetchall()
        cursor.close()
        return all_rows


class Users_DB:
    def __init__(self):
        self.users = {}
