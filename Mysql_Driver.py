import mysql.connector
from mysql.connector import Error

class MysqlQuery:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connect = None
        self.cursor = None

    def deleteTable(self, device_tab):
        sql_drop_tab_query = "DROP TABLE " + device_tab
        self.cursor.execute(sql_drop_tab_query)
        print("Delete table " + device_tab + " successfully!\n")

    def connectDatabase(self):
        try:
            self.connect = mysql.connector.connect(host=self.host,
                                        database=self.database,
                                        user=self.user,
                                        password=self.password)
            if self.connect.is_connected():
                self.cursor = self.connect.cursor()     
                print("Connected to MySQL database")
        except mysql.connector.Error as error:
            print("Failed to connect to database!")
            
    def insertTable(self,device_tab, data):
        sql_insert_query = "INSERT INTO "+ device_tab + "(DATA) VALUES('" + data + "')"
        self.cursor.execute(sql_insert_query)
        self.connect.commit()
        print("Insert into database successfully!")

    def readAllTable(self, device_tab):
        sql_read_all_query = "SELECT * FROM "+ device_tab + ";"
        self.cursor.execute(sql_read_all_query)
        records = self.cursor.fetchall()
        for row in records:
            print(row)

    def readRecentTable(self, device_tab, size_row):
        sql_read_recent_query = "SELECT * FROM "+ device_tab + " ORDER BY TIME DESC;"
        self.cursor.execute(sql_read_recent_query)
        records = self.cursor.fetchmany(size_row)
        for row in records:
            print(row)

    def deleteDataTable(self):
        sql_delete_query = "TRUNCATE mqtt_data;"
        self.cursor.execute(sql_delete_query)
        self.connect.commit()
        print("Delete database successfully!\n")
 
    def finishConnect(self):
        if(self.connect.is_connected()):
              self.cursor.close()
              self.connect.close()
              print("MySQL connection is closed\n")
