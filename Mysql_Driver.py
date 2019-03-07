import mysql.connector
from mysql.connector import Error

class MysqlQuery:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connectDatabase(self):
        connection = mysql.connector.connect(host=self.host,
                                    database=self.database,
                                    user=self.user,
                                    password=self.password)
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection

    def insertDatabase(self, conn):
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to - ", record)
        sql_insert_query = "INSERT INTO mqtt_data(DATA) VALUES('HELLO')"
        cursor.execute(sql_insert_query)
        conn.commit()
        return cursor

    def finishConnect(self, conn, curs):
         if(conn.is_connected()):
              curs.close()
              conn.close()
              print("MySQL connection is closed")


# conn = connectDatabase()
# curs = insertDatabase(conn)
# finishConnect(conn, curs)