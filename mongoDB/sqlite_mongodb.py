"""
Pipeline example from sqlite to mongodb
"""
import sqlite3
# from typing_extensions import ParamSpecArgs
import pymongo

PASSWORD = 'ffkNZJKrtsDO5cxI'
DBNAME = 'nwdelafu-WinOS'


def connect_to_mongo(password, dbname):
    client = pymongo.MongoClient(
        "mongodb+srv://nwdelafu-WinOS:{}@cluster0.hkp4s.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
        )
    return client


def connect_to_sldb():
    conn = sqlite3.connect('../data/rpg_db.sqlite3')
    curs = conn.cursor()
    return conn, curs


def handle_item(curs):
    """
    handle_item Generate a dictionary to hold items for each character

    Args:
        curs ([type]): [description]
    """
    # inventory_char = {'1':[]}
    weapon_list = curs.execute(
    f"""SELECT name, item_ptr_id
        FROM
        (SELECT * FROM charactercreator_character_inventory as cii
        LEFT JOIN armory_item as ai
        ON cii.item_id = ai.item_id) as a
        LEFT JOIN armory_weapon as aw
        ON a.item_id=aw.item_ptr_id
        WHERE character_id=5;
    """)
    inventory_char = [weapon[0] for weapon in weapon_list if weapon[1] != None]
    # for weapon in weapon_list:
    #     if weapon[1] != None:
    #         inventory_char['1'].append(weapon[0])
    return inventory_char


def handle_characters(curs, collection):
    """
    handle_characters Handles character pipeline
    """
    character_list = curs.execute("""SELECT * FROM charactercreator_character;""")
    for character in character_list:
        _, sl_curs = connect_to_sldb() # need to create a different cursor because the main one still 
                                        # running and it will close the whole thing before it loop
        # item_list = sl_curs.execute(
        #     f"""SELECT ai.name FROM charactercreator_character_inventory as cii
        #         LEFT JOIN armory_item as ai
        #         ON cii.item_id = ai.item_id
        #         WHERE character_id={character[0]};
        #     """)
        inventory = sl_curs.execute(
            f"""SELECT name, item_ptr_id
                FROM
                (SELECT * FROM charactercreator_character_inventory as cii
                LEFT JOIN armory_item as ai
                ON cii.item_id = ai.item_id) as a
                LEFT JOIN armory_weapon as aw
                ON a.item_id=aw.item_ptr_id
                WHERE character_id={character[0]};
            """).fetchall()

        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8],
            "items": [item[0] for item in inventory],
            "weapons": [item[0] for item in inventory if item[1] != None]
        }
        sl_curs.close() # close that new cursor
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
    # table = handle_item(sl_curs)
    # print(table)
    sl_curs.close()

