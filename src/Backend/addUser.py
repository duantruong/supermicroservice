import bcrypt, mysql.connector
from Connection import get_sql_connection
pw_hash = bcrypt.hashpw("Theduan1997".encode(), bcrypt.gensalt()).decode()
conn = get_sql_connection(); cur = conn.cursor()
cur.execute("INSERT INTO users(email,password) VALUES(%s,%s)",("me@example.com", pw_hash))
conn.commit(); cur.close(); conn.close()
