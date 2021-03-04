import mysql.connector
from pr import pwd

myDb = mysql.connector.connect(host='localhost', user='root', password=pwd)
myCursor = myDb.cursor()

myCursor.execute("CREATE DATABASE my_db1")