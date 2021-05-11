"""
    A bsic PostGreSQL workflow
"""
import psycopg2 as pg2
from queries import SQL_CREAT_TABLE, SQL_INSERT_DATA, SQL_SHOW_TABLE


DBNAME = 'xesxjqea'
USER = "xesxjqea"
PASSWORD = "nSNnSBldNahsOI2Hj9wVeru17t8i_fpt"
HOST = "queenie.db.elephantsql.com"

def create_connection(dbname, user, password, host):
    pg_conn = pg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
    return pg_conn


def execute_query(conn, query, read=True):
    pg_curs = conn.cursor()
    pg_curs.execute(query)
    if read:
        # Will fetch data if we are reading so we don't get error
        results = pg_curs.fetchall()
        pg_curs.close()
        return results
    else:
        # Will commit our changes if we are Creating, Updating, Deleting
        conn.commit()
        pg_curs.close()
        return "CUD Query Executted"


def show_test_table(conn):
    pg_curs = conn.cursor()
    pg_curs.execute(SQL_SHOW_TABLE)
    return pg_curs.fetchall()


if __name__ == "__main__":
    pg_conn = create_connection(DBNAME, USER, PASSWORD, HOST)
    execute_query(conn=pg_conn, query=SQL_CREAT_TABLE, read=False)
    execute_query(conn=pg_conn, query=SQL_INSERT_DATA, read=False)
    results = show_test_table(pg_conn)
    print(results)