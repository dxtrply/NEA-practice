import sqlite3 as sql

class DatabaseHandler:
    def __init__(self, databaseName = "appData.db"):
        self.databaseName = databaseName

    def createTables(self):
        conn = sql.connect(self.databaseName)
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                            username TEXT PRIMARY KEY NOT NULL,
                            password TEXT NOT NULL,
                            CHECK( length(password) >= 8)
                       )""")

        conn.close()
    ##CRUD
    def createUser(self):
        pass

    def createUser(self):
        pass

    def readUser(self):
        pass

    def updateUser(self):
        pass

    def deleteUser(self):
        pass