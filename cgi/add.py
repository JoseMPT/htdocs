#!C:/Users/black/AppData/Local/Programs/Python/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print('Content-Type: text/html\n')
print("<h1>Agregar usuarios<hr></h1>")

method = os.environ['REQUEST_METHOD']
if method == 'POST':
    data = cgi.FieldStorage()
    email = data.getvalue(key='email')
    password = data.getvalue(key='password')
    name = data.getvalue(key='name')
    avatar = data.getvalue(key='avatar')
    role = data.getvalue(key='role')
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='forumdb')
    cur = con.cursor()
    sql = "INSERT INTO users VALUES('{}',sha1('{}'),'{}','{}','{}')".format(email, password, name, avatar, role)
    cur.execute(sql)
    con.commit()
    con.close()
    print('<h2>Usuario agregado</h2>')
else:
    print('<h4>Método erróneo</h4>')
