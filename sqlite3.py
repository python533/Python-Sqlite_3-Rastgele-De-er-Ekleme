import sqlite3
import random
import time
import datetime

def veritabanı():
    con = sqlite3.connect("")
    cursor = con.cursor()

def tabloolustur(cursor):
    def tabloolustur():
        cursor.execute("CREATE TABLE IF NOT EXISTS tablo1 (zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")

def rastgeledegerekle(cursor):
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman). strftime('%Y-%m-%d : %H:%M:%S'))
    anahtarkelime ='pythonsqlite3'
    deger =random.randrange(0,10)
    cursor.execute("INSERT INTO tablo1(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))


def verial(cursor):
    cursor.execute("SELECT * FROM tablo1")
    data=cursor.fetchall()
    for i in data:
        print(i)







        
