#!C:/Users/black/AppData/Local/Programs/Python/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print('Content-Type: text/html\n')
print("<h1>Eliminar usuario<hr></h1>")

method = os.environ['REQUEST_METHOD']
if method == 'POST':
    data = cgi.FieldStorage()
    email = data.getvalue(key='email')
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='forumdb')
    cur = con.cursor()
    sql = "DELETE FROM users WHERE email='{}';".format(email)
    cur.execute(sql)
    con.commit()
    con.close()
    print('<h2>Usuario eliminado</h2>')
else:
    print('<h4>Método erróneo</h4>')