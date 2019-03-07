from Mysql_Driver import MysqlQuery

HOST = 'localhost'
DATABASE = 'MQTT_DATABASE'
USER = 'root'
PASSWORD = '123456'

#Create object via contructor method __init__
mysqlQuery = MysqlQuery(HOST, DATABASE, USER, PASSWORD)

"""Step to implement QUERY command to MySQL database
	1. Create MySQL database connection and cursor object to
		perform Database Operation
	2. Define MySQL queries such as INSERT, SELECT, DELETE
	3. Close database connection""" 

mysqlQuery.connectDatabase()
# mysqlQuery.insertTable("mqtt_data", "hello world")
# mysqlQuery.deleteDataTable()
# mysqlQuery.readAllTable("mqtt_data")
mysqlQuery.readRecentTable("mqtt_data", 2)
mysqlQuery.finishConnect()
