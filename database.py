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
    def createUser(self, username, password):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO users VALUES(?, ?) """, (username, password))
            conn.commit()

            conn.close()
            return True, "sign up successful"
        except:
            return False, "an error occured signing up"
        finally:
            conn.close()

    def readUser(self):
        pass

    def updateUser(self):
        pass

    def deleteUser(self):
        pass