#!/usr/bin/python3
import MySQLdb
import sys
'''
script to get states
'''

if __name__ == '__main__':

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=arg1, passwd=arg2, db=arg3, charset="utf8")

    cur = conn.cursor()
    
    
    query = '''
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    '''
    

    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
