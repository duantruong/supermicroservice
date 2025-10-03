import os
import mysql.connector
from mysql.connector import pooling

_pool = pooling.MySQLConnectionPool(
    pool_name="main_pool",
    pool_size=5,
    host=os.getenv("DB_HOST", "127.0.0.1"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASS", ""),
    database=os.getenv("DB_NAME", "supermicro"),
    port=int(os.getenv("DB_PORT", "3306")),
)

def get_sql_connection():
    return _pool.get_connection()
