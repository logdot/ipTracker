import urllib.request
import json
import re
import sqlite3
import os
import time
import datetime

def getThreads():
    threads = []

    with urllib.request.urlopen("https://a.4cdn.org/vt/catalog.json") as url:
        data = url.read()
        data = json.loads(data)

        temp = []
        for page in data:
            for thread in page['threads']:
                try: # I'm fairly certain this isn't proper
                    if 'wah' in thread['sub'].lower():
                        temp.append(thread)
                except:
                    pass

        for t in temp:
            time.sleep(1) # Ensure 1 second between requests
            with urllib.request.urlopen(f"https://a.4cdn.org/vt/thread/{t['no']}.json") as url:
                data = url.read()
                data = json.loads(data)
                t = list(data['posts'])[0]

                thread = Thread(t['no'], t['now'], t['name'], t['sub'], t['replies'], t['images'], t['unique_ips'])

                threads.append(thread)
                Thread.addToBuffer(thread)
    return threads


class Thread:
    threads = []
    buffer = []
    init = False

    def __init__(self, idd, now, name, sub, replies, images, ips):
        self.idd = idd
        self.now = now 
        self.name = name
        self.sub = sub
        self.replies = replies
        self.images = images
        self.ips = ips

    @classmethod
    def addToBuffer(cls, thread):
        cls.buffer.append(thread)


    @classmethod
    def pushBuffer(cls):
        for t in cls.buffer:
            addThread(t)


    def getDay(self):
        return self.now[11:14]


    @classmethod
    def initialize(cls):
        if not cls.init:
            Thread.readThreads()
            cls.init = True


    @classmethod
    def addThread(cls, thread):
        old = False
        for i in range(len(cls.threads)):
            if cls.threads[i].idd == thread.idd:
                old = True
                cls.threads[i] = thread

        if not old:
            Thread.threads.append(self)


    @classmethod
    def readThreads(cls):
        con = sqlite3.connect("wahThreads.db")
        cur = con.cursor()

        for thread in cur.execute('SELECT * FROM Threads WHERE id != 0'):
            Thread(thread[0], thread[1], thread[2], thread[3], thread[4], thread[5], thread[6])
        con.close()

        return cls.threads


    @classmethod
    def getAllIds(cls):
        ids = []
        for thread in cls.threads:
            ids.append(thread.idd)

        return ids


    @classmethod
    def getAllIps(cls):
        ips = []
        for thread in cls.threads:
            ips.append(thread.ips)

        return ips


    @classmethod
    def getAllDates(cls):
        dates = []
        for thread in cls.threads:
            dates.append(thread.now)

        return dates 
    

    @classmethod
    def getAllDays(cls):
        days = []
        for thread in cls.threads:
            days.append(thread.now[11:14])

        return days


    @classmethod
    def getAllReplies(cls):
        replies = []
        for thread in cls.threads:
            replies.append(thread.replies)

        return replies


    @classmethod
    def getAllDatetimes(cls):
        datetimes = []
        for thread in cls.threads:
            year = 21
            month = int(thread.now[0:2])
            day = int(thread.now[4:6])

            hour = int(thread.now[15:17])
            minute = int(thread.now[18:20])
            second = int(thread.now[21:23])

            datetimes.append(datetime.datetime(year, month, day, hour, minute, second, 0))

        return datetimes



# Create table if the file database doesn't exist
if not os.path.exists("wahThreads.db"):
    print("Creating database")
    con = sqlite3.connect("wahThreads.db")
    cur = con.cursor()
    cur.execute('''
            CREATE TABLE Threads (
            id INTEGER PRIMARY KEY UNIQUE,
            now STRING NOT NULL,
            name STRING NOT NULL,
            sub STRING NOT NULL,
            replies INTEGER NOT NULL,
            images INTEGER NOT NULL,
            ips INTEGER NOT NULL)''')
    con.commit()
    con.close()

if __name__ == '__main__':
    Thread.initialize()

    con = sqlite3.connect("wahThreads.db")
    cur = con.cursor()

    for thread in Thread.threads:
        print(thread.idd)

    while True:
        try:
            newThreads = getThreads()
        except:
            print("Not able to get threads, sleeping")
            time.sleep(300)
            continue

        # Show updated threads
        for newThread in newThreads:
            print(f"Updating: {newThread.idd}")
        Thread.pushBuffer()
 
        for thread in Thread.threads:
            cur.execute('INSERT or REPLACE INTO Threads VALUES (?, ?, ?, ?, ?, ?, ?)', 
                    (int(thread.idd),
                    thread.now, 
                    thread.name, 
                    thread.sub, 
                    int(thread.replies),
                    int(thread.images),
                    int(thread.ips)))

        con.commit()

        print("Sleeping")
        time.sleep(60)
