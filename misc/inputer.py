from iptracker import Thread
import sqlite3

Thread.initialize()

con = sqlite3.connect("wahThreads.db")
cur = con.cursor()

while True:
    idd = input("ID: ")
    now = input("now: ")
    name = input("name: ")
    sub = input("subtitle: ")
    replies = input("replies: ")
    images = input("images: ")
    ips = input("ip #: ")

    cur.execute('INSERT or REPLACE INTO Threads VALUES (?, ?, ?, ?, ?, ?, ?)', 
            (int(idd),
            now, 
            name, 
            sub, 
            int(replies),
            int(images),
            int(ips)))

    con.commit()
