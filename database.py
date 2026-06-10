import sqlite3 as sql
from unittest import result

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
        

        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
                        taskId INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        username TEXT NOT NULL,
                        CHECK (length(description) >= 3),
                        FOREIGN KEY (username) REFERENCES users(username)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
                        )
                        )""")

        cursor.execute("PRAGMA foreign_keys = ON")

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

    def readUserPasswordHash(self,username):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = ?", (username, ))
            results = cursor.fetchone()
            return True, results
        except:
            return False, "An error occured when logging in."
        finally:
            conn.close

            print(results)




    def updateUser(self):
        pass

    def deleteUser(self):
        pass

    def createTask(self, description, username):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO tasks (description, username)
                            values
                            (?, ?)""", (description, username))

            conn.commit()
            return True, "Task created successfully"
        except:
            return False, "an error occured making task"
        finally:
            conn.close()
        
    def readALLTasks(self, username):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()
            cursor.execute("""SELECT taskId, description FROM tasks WHERE username = ?""", (username, ))
            cursor.fetchall()
            return True, result
    
        except:
            return False, [] #blank list showing no tasks
        finally:
            conn.close()