import sqlite3

class DBApi:

    def __init__(self):
        # TODO: Current League name. New DB for each league (so we can easily search through recent leagues as well and have an easier time working with data)
        self.con = sqlite3.connect('development.db')
        self.cur = self.con.cursor()

        # Create Table
        self.cur.execute('''CREATE TABLE IF NOT EXISTS stashDb (id INTEGER PRIMARY KEY, time INTEGER NOT NULL, action TEXT NOT NULL, item TEXT NOT NULL, account TEXT NOT NULL)''')
        self.con.commit()

    def insert(self, entry):
        self.cur.execute("INSERT INTO stashDb VALUES ({0}, {1}, {2}, {3}, {4})".format(int(entry["id"]), int(entry["time"]), str(entry["item"]), str(entry["action"]), str(entry["account"]["name"])))
        self.con.commit()

    def insertMany(self, entries):
        # Prepare data for insertion
        insertList = []
        for entry in entries:
            insertEntry = (int(entry["id"]), int(entry["time"]), str(entry["action"]), str(entry["item"]), str(entry["account"]["name"]))
            insertList.append(insertEntry)

        self.cur.executemany("INSERT INTO stashDb VALUES (?, ?, ?, ?, ?)", insertList)
        self.con.commit()

    def findLatestRecord(self):
        self.cur.execute("select id, MAX(time) from stashDb")
        response = self.cur.fetchall()
        latestRecord = response[0]

        return {"id": str(latestRecord[0]), "time": str(latestRecord[1])}