"""
    SQLite to PostGresQL pipeline
"""

import sqlite3
import psycopg2 as pg2
import queries as q
import pandas as pd


DBNAME = 'xesxjqea'
USER = "xesxjqea"
PASSWORD = "nSNnSBldNahsOI2Hj9wVeru17t8i_fpt"
HOST = "queenie.db.elephantsql.com"
DATA_PATH = '../data/titanic.csv'

df = pd.read_csv(DATA_PATH)
df['Pclass'] = df['Pclass'].astype(str)
# print(df.iloc[1])
# print(df.isna().sum().sum())
# print(df.describe(exclude='number'))
# after doing some data exploration the data is super clean without NULL
# and duplicates entry


# # We want to move charactercreator_character from sqlite --> postgresql
def create_connections(dbname, user, password, host, sqlite_db='../data/titanic.sqlite3'):
    """
    create_connection to sqlite and postgresql

    """
    sl_conn = sqlite3.connect(sqlite_db)
    pg_conn = pg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
    return sl_conn, pg_conn


def execute_query(conn, query, read=True):
    """Executes queries depending on conn object passed in"""
    curs = conn.cursor()
    curs.execute(query)
    if read:
        # Will fetch data if we are reading so we don't get error
        results = curs.fetchall()
        curs.close()
        return results
    else:
        # Will commit our changes if we are Creating, Updating, Deleting
        conn.commit()
        curs.close()
        return "CUD Query Executed"


if __name__ == "__main__":
    sl_conn, pg_conn = create_connections(DBNAME, USER, PASSWORD, HOST)
    #df.to_sql('titanic', sl_conn)
    # extract and make a item list
    titanic_row = execute_query(sl_conn, q.EXTRACT_TITANIC)
    execute_query(
        conn=pg_conn, query=q.CREATE_titanic, read=False
    )
    pg_curs = pg_conn.cursor()
    #pg_curs.execute(q.COPY_titanic) --> need superuser
    for row in titanic_row:
        pg_curs.execute(q.INSERT_INTO_titanic, row)
        pg_conn.commit()
    pg_curs.close()
