from Mysql_Driver import MysqlQuery

HOST = 'localhost'
DATABASE = 'MQTT_DATABASE'
USER = 'root'
PASSWORD = '123456'

#Create object via contructor method __init__
mysqlQuery = MysqlQuery(HOST, DATABASE, USER, PASSWORD)

#Implement query command to insert data into database
conn = mysqlQuery.connectDatabase()
curs = mysqlQuery.insertDatabase(conn)
mysqlQuery.finishConnect(conn, curs)