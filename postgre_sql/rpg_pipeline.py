"""
    SQLite to PostGresQL pipeline
"""

from os import read
import sqlite3
import psycopg2 as pg2
import queries as q


DBNAME = 'xesxjqea'
USER = "xesxjqea"
PASSWORD = "nSNnSBldNahsOI2Hj9wVeru17t8i_fpt"
HOST = "queenie.db.elephantsql.com"


# We want to move charactercreator_character from sqlite --> postgresql
def create_connections(dbname, user, password, host, sqlite_db='../data/rpg_db.sqlite3'):
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

    # extract and make a character list
    character_list = execute_query(sl_conn, q.EXTRACT_CHARACTERS)
    # character_list = [(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1), (...), (...), ...]
    execute_query(
        conn=pg_conn, query=q.CREATE_charactercreator_character, read=False
    )

    # extract and make a item list
    item_list = execute_query(sl_conn, q.EXTRACT_ITEMS)
    execute_query(
        conn=pg_conn, query=q.CREATE_armory_item, read=False)

    # extract and make an inventory list
    inventory_list = execute_query(sl_conn, q.EXTRACT_INVENTORY)
    execute_query(
        conn=pg_conn, query=q.CREATE_charactercreator_character_inventory, read=False
    )

    # extract and make a weapon list
    weapon_list = execute_query(sl_conn, q.EXTRACT_WEAPON)
    execute_query(
        conn=pg_conn, query=q.CREATE_armory_weapon, read=False
    )

    # extract and make a mage list
    mage_list = execute_query(sl_conn, q.EXTRACT_MAGE)
    execute_query(
        conn=pg_conn, query=q.CREATE_charactercreator_mage, read=False
    )

    pg_curs = pg_conn.cursor()

    for character in character_list:
        pg_curs.execute(q.INSERT_INTO_charactercreator_character, character[1:])
        pg_conn.commit()
    for item in item_list:
        pg_curs.execute(q.INSERT_INTO_armory_item, item[1:])
        pg_conn.commit()
    for inventory in inventory_list:
        pg_curs.execute(q.INSERT_INTO_charactercreator_character_inventory, inventory)
        pg_conn.commit()
    for weapon in weapon_list:
        pg_curs.execute(q.INSERT_INTO_armory_weapon, weapon)
        pg_conn.commit()    
    for mage in mage_list:
        pg_curs.execute(q.INSERT_INTO_charactercreator_mage, mage)
        pg_conn.commit()
    
    pg_curs.close()