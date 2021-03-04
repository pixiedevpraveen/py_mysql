import mysql.connector
from .pr import pwd

myDb = mysql.connector.connect(host='localhost', user='root', password=pwd)

print(myDb.connection_id)