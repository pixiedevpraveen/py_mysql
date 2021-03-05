import mysql.connector

from pr import pwd

myDb = mysql.connector.connect(
    host='localhost', user='root', password=pwd, database='my_db1')

myCursor = myDb.cursor()
command = "UPDATE book SET price=price+40 WHERE price<300"

# for execute the query
myCursor.execute(command)

# for reflect changes to database
myDb.commit()
