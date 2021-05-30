import sqlite3

class DBApi:

    def __init__(self):
        # TODO: Current League name. New DB for each league (so we can easily search through recent leagues as well and have an easier time working with data)
        self.con = sqlite3.connect('development.db')
        self.cur = self.con.cursor()

        # Create Table
        self.cur.execute('''CREATE TABLE IF NOT EXISTS stashDb (id INTEGER PRIMARY KEY, time INTEGER NOT NULL, action TEXT NOT NULL, item TEXT NOT NULL, account TEXT NOT NULL)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS memberDb (name TEXT PRIMARY KEY, chaos_delta INTEGER NOT NULL)''')
        self.con.commit()

    def insertManyTransactions(self, entries):
        # Prepare data for insertion
        insertList = []
        for entry in entries:
            insertEntry = (int(entry["id"]), int(entry["time"]), str(entry["action"]), str(entry["item"]), str(entry["account"]["name"]))
            insertList.append(insertEntry)

        self.cur.executemany("INSERT INTO stashDb VALUES (?, ?, ?, ?, ?)", insertList)
        self.con.commit()

    def insertManyMembers(self, entries):
        # Prepare data for insertion
        insertList = []
        for entry in entries:
            insertEntry = (str(entry["account"]["name"]), 0)
            insertList.append(insertEntry)

        self.cur.executemany("INSERT OR IGNORE INTO memberDb VALUES (?, ?)", insertList)
        self.con.commit()

    def findLatestRecord(self):
        self.cur.execute("select id, MAX(time) from stashDb")
        response = self.cur.fetchall()
        latestRecord = response[0]

        return {"id": str(latestRecord[0]), "time": str(latestRecord[1])}

    def getAllMembers(self):
        self.cur.execute("select * from memberDb")
        return self.cur.fetchall()

    def getAllTransactionsOfMember(self, member):
        self.cur.execute("select * from stashDb where account='{0}'".format(member[0]))
        return self.cur.fetchall()