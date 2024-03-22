#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
import MySQLdb as ms
from sys import argv


host = "localhost"
user = argv[1]
passwd = argv[2]
db = argv[3]

db = ms.connect(host=host, user=user, passwd=passwd, db=db, port=3306)


if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("SELECT * FROM Customers;")
    
    print(*cur.fetchall(), sep="\n")
    db.close()
