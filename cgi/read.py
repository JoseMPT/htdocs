#!C:/Users/black/AppData/Local/Programs/Python/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print('Content-Type: text/html\n')
print("<h1>Consulta usuarios</h1><hr>")

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='forumdb')
cur = con.cursor()
sql = 'SELECT * FROM users'
cur.execute(sql)

for (email, password, name, avatar, role) in cur:
    print('{}, {}, {}, {}, {}<br>'.format(email, password, name, avatar, role))
