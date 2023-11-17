#!/usr/bin/python3
""" lists all states from db hbtn_0e_0_usa where name matches
    argument - protected from SQL injection """


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    name = sys.argv[4]
    mycursor.execute("SELECT * FROM states WHERE name LIKE %s"
                     "ORDER BY id ASC", (name, ))
    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    db.close()
