import mysql.connector

from pr import pwd

myDb = mysql.connector.connect(
    host='localhost', user='root', password=pwd, database='my_db1')

myCursor = myDb.cursor()
command = "CREATE TABLE book(bookid integer(4), title varchar(20), price float(5,2))"
myCursor.execute(command)