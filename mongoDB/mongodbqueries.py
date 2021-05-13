import sqlite3
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


def number_char(collection):
    result = collection.count_documents({})
    print(result)


def total_items(collection):
    result = collection.distinct('items')
    print(len(list(result)))


def total_weapons(collection):
    result = collection.distinct('weapons')
    print(len(list(result)))


def item_each_char(collection):
    docs = collection.find().limit(20)
    for doc in docs:
        print(len(doc['items']))


def weapon_each_char(collection):
    docs = collection.find().limit(20)
    for doc in docs:
        print(len(doc['weapons']))



if __name__ == "__main__":
    mongo_client = connect_to_mongo(PASSWORD, DBNAME)
    # sl_conn, sl_curs = connect_to_sldb()
    collection = mongo_client.myFirstDatabase.myFirstDatabase
    # collection.delete_many({})
    number_char(collection)
    # print(list(collection.find()))
    # sl_curs.close()