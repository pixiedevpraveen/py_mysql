import mysql.connector

from pr import pwd

myDb = mysql.connector.connect(
    host='localhost', user='root', password=pwd, database='my_db1')

myCursor = myDb.cursor()
command = "INSERT INTO book (bookid, title, price) VALUES(%s, %s, %s)"

sno = 1
book_name = "Let us C"
price = 275

# tuple
book1 = (sno, book_name, price)

# for execute the query
myCursor.execute(command, book1)

# for storing data or reflect changes to created database
myDb.commit()