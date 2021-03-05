import mysql.connector

from pr import pwd

myDb = mysql.connector.connect(
    host='localhost', user='root', password=pwd, database='my_db1')

myCursor = myDb.cursor()
command = "SELECT * FROM book"

# for execute the query
myCursor.execute(command)

# fetchall data returns a list of tuples
responses = myCursor.fetchall()

# printing values of tuples from the list
for response in responses:
    print(response)