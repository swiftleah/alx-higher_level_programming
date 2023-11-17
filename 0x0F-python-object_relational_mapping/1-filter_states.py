#!/usr/bin/python3
""" lists all states from db hbtn_0e_0_usa that start with 'N' """


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id states.id")
    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    db.close()
