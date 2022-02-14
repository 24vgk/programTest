import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser

home = expanduser('~')
sql_hostname = 'localhost'
sql_username = 'admin'
sql_password = 'V1qaz2wsx'
sql_main_database = 'testDB'
sql_port = 3306
ssh_host = '194.67.105.196'
ssh_user = 'root'
ssh_port = 22
ssh_password ='jFuJ7p$KTX?3'
sql_ip = '1.1.1.1.1'
with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
    conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            passwd=sql_password, db=sql_main_database,
            port=tunnel.local_bind_port)
    query = '''SELECT VERSION();'''
    data = pd.read_sql_query(query, conn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
        print(row[2])
    conn.close()