from werkzeug.security import check_password_hash
from connection import get_sql_connection

def authenticate(email: str, password: str) -> bool:
    sql = "SELECT password FROM users WHERE email=%s"
    with get_sql_connection() as conn, conn.cursor(dictionary=True) as cur:
        cur.execute(sql, (email.lower().strip(),))
        row = cur.fetchone()
    return bool(row and check_password_hash(row["password"], password))
