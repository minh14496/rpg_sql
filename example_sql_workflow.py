import sqlite3
from queries import SELECT_CHARACTERS

# STEP 1: Connect to the database
def connect_to_db(db_name='data/rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

# STEP 2: Make a cursor from our connection
# STEP 4: Execute Query
# STEP 5: Fetch results
def execute_query(conn, query):
    curs = conn.cursor()
    results = curs.execute(query).fetchall()
    curs.close()
    return results

    
if __name__ == "__main__":
    conn = connect_to_db()
    execute_query(conn, SELECT_CHARACTERS)