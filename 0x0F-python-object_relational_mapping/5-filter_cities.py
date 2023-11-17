#!/usr/bin/python3
""" takes in name of state as argument(4) and lists all cities of that state
    using database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    mycursor = db.cursor()
    mycursor.execute("""SELECT cities.name FROM cities INNER
                     JOIN states ON states.id=cities.state_id
                     WHERE states.name=%s""", (sys.argv[4],))
    result = mycursor.fetchall()
    cities = [row[0] for row in result]

    print(", ".join(cities))
