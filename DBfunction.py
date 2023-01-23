import sqlite3


class sqliteDB:
    def __init__(self, db_name, table_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.table = table_name

    def createTable(self, columns):
        column = "("
        for col in columns:
            column = column + f"{col[0]} {col[1]},"  # col[0] = column name / col[1] = datatype
        column = column[:-1]
        column += ")"
        command = f"CREATE TABLE {self.table}{column}"

        self.cursor.execute(command)

    def insertTable(self, rows):
        command = "INSERT INTO " + self.table + " VALUES(?,?)"
        self.cursor.execute(command , (rows[0],rows[1]))

    def selectaTableall(self):
        command = f"SELECT * FROM {self.table}"

        self.cursor.execute(command)

        return self.cursor.fetchall()

    def updataTable(self, col_set, col_where, data_set, data_where):
        command = f"UPDATE {self.table} SET {col_set}=? WHERE {col_where}=?"

        self.cursor.execute(command, (data_set, data_where))

    def deleteTable(self, col_where, data_where):
        command = f"DELETE FROM {self.table} WHERE {col_where}=?"
        self.cursor.execute(command, ({data_where},))

    def commitTable(self):
        self.connect.commit()
