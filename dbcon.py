import MySQLdb
import sys
import json
connection = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'tst')
cursor = connection.cursor()
cursor.execute('SELECT * from orders')
row = cursor.fetchone()
json.loads(row)
cursor.close()
connection.close()