#!/usr/bin/python3
""" lists all cities from database hbtn_0e_4_usa """


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()
    mycursor.execute("""SELECT cities.id, cities.name, states.name FROM
                     cities JOIN states ON cities.state_id = states.id ORDER BY
                     cities.id ASC""")

    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    db.close()
