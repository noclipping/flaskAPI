import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        host='ep-misty-forest-a5xuun9v.us-east-2.aws.neon.tech',
        database='test_db',
        user='test_db_owner',
        password='PRs26LBWewTx'
    )
    return conn