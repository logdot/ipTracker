from iptracker import Thread
import sqlite3

Thread.initialize()

con = sqlite3.connect("wahThreads.db")
cur = con.cursor()

while True:
    idd = input("ID: ")

    cur.execute("DELETE from Threads where id = (?)", (idd,))
    con.commit()
