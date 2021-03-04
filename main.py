import mysql.connector

from pr import pwd

myDb = mysql.connector.connect(
    host='localhost', user='root', password=pwd, database='my_db1')

myCursor = myDb.cursor()
command = "INSERT INTO book (bookid, title, price) VALUES(%s, %s, %s)"

# list of tuples
books = {(2, 'Learn C++', 250), (3, 'Data structure', 350),
         (4, 'Java8', 300)}

# for execute the query
myCursor.executemany(command, books)

# for storing data or reflect changes to created database
myDb.commit()
