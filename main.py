import mysql.connector

from pr import pwd

myDb = mysql.connector.connect(
    host='localhost', user='root', password=pwd, database='my_db1')

myCursor = myDb.cursor()

# 'DELETE FROM book' don't execute this
# it'll delete all the data of book
command = "DELETE FROM book WHERE title='Java8'"

# for execute the query
myCursor.execute(command)

# for reflect changes to database
myDb.commit()
