#!/usr/bin/python3
'''
script to get states
'''
import MySQLdb
import sys

if __name__ == '__main__':

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=arg1,
                                passwd=arg2, db=arg3, charset="utf8")

    cur = conn.cursor()

    query = '''
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    '''

    cur.execute(query, (state_name,))

    query_rows = cur.fetchall()
    cities = []
    for row in query_rows:
        cities.append(row[1])
    print(", ".join(cities))

    cur.close()
    conn.close()
