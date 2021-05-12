"""
Pipeline example from sqlite to mongodb
"""
import sqlite3
from typing_extensions import ParamSpecArgs
import pymongo

PASSWORD = 'ffkNZJKrtsDO5cxI'
DBNAME = 'nwdelafu-WinOS'


def connect_to_mongo(password, dbname):
    client = pymongo.MongoClient(
        "mongodb+srv://nwdelafu-WinOS:{}@cluster0.hkp4s.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
        )
    return client


def connect_to_sldb(dbname="../data/rpg_db.sqlite3"):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    return conn, curs


def handle_characters(curs, collection):
    """
    handle_characters Handles character pipeline
    """
    character_list = curs.execute("""SELECT * FROM charactercreator_character;""")
    for character in character_list:
        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8],
            # "items": TODO: Assignment
            # "weapons": TODO: Assignment
        }
        collection.insert_one(character_doc)

    # # A codier way to do it
    # schema = curs.execute(
    #     "PRAGMA table_info(charactercreator_character)").fetchall()[1:]
    # for character in characters_list:
    #     character_doc = {}
    #     for index, item_tuple in enumerate(schema):
    #         character_doc[item_tuple[1]] = character[index + 1]

    #     collection.insert_one(character_doc)

if __name__ == "__main__":
    mongo_client = connect_to_mongo(PASSWORD, DBNAME)
    sl_conn, sl_curs = connect_to_sldb()
    collection = mongo_client.myFirstDatabase.myFirstDatabase
    collection.delete_many({})
    handle_characters(sl_curs, collection)
    print(list(collection.find()))
    sl_curs.close()

