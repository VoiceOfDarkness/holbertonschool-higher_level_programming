import MySQLdb as ms
from sys import argv


host = "localhost"
user = argv[1]
passwd = argv[2]
db = argv[3]

db = ms.connect(host=host, user=user, passwd=passwd, db=db)


def list_all_states():
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    return cur.fetchall()


if __name__ == "__main__":
    print(*list_all_states(), sep="\n")
    db.close()
