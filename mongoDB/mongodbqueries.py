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
    """
    number_char Count the number of documents in colleciton
    """
    result = collection.count_documents({})
    return result


def total_items(collection):
    """The number of distinct items in inventory 
    or the total of items in armory_item"""
    result = collection.distinct('items')
    return len(list(result))


def total_item_in_inventory(collection):
    """The total number of items in inventory"""
    result = collection.aggregate([
        {
            '$project': {
                'lenOfItem': {'$size': "$items"}

            }
        }, 
        {
            '$group': 
            {
                '_id': None, 'sum': {'$sum': '$lenOfItem'}
            }
        }
    ])
    return list(result)


def total_weapons(collection):
    """The number of distinct weapons in inventory 
    or the total of items in armory_weapon"""
    result = collection.distinct('weapons')
    return len(list(result))


def total_weapon_in_inventory(collection):
    """The total number of weapons in inventory"""
    result = collection.aggregate([
        {
            '$project': {
                'lenOfWeapon': {'$size': "$weapons"}

            }
        }, 
        {
            '$group': 
            {
                '_id': None, 'sum': {'$sum': '$lenOfWeapon'}
            }
        }
    ])
    return list(result)


def item_each_char(collection):
    # docs = collection.find().limit(20)
    # for doc in docs:
    #     print(len(doc['items']))
    """The number of items each character have"""
    result = collection.aggregate([
        {
            '$project': {
                'lenOfItem': {'$size': "$items"}
            }
        }, {'$limit': 20}
    ])
    return list(result)


def weapon_each_char(collection):
    # docs = collection.find().limit(20)
    # for doc in docs:
    #     print(len(doc['weapons']))
    """The number of weapons each character has"""
    result = collection.aggregate([
        {
            '$project': {
                'lenOfWeapon': {'$size': "$weapons"}

            }
        }, {'$limit': 20}
    ])
    return list(result)


def average_item_char(collection):
    """The average number of items each character have"""
    result = collection.aggregate([
        {
            '$project': {
                'lenOfItem': {'$size': "$items"}

            }
        }, 
        {
            '$group': 
            {
                '_id': None, 'avg': {'$avg': '$lenOfItem'}
            }
        }
    ])
    return list(result)


def average_weapon_char(collection):
    """The average number of weapons each character have"""
    result = collection.aggregate([
        {
            '$project': {
                'lenOfWeapon': {'$size': "$weapons"}

            }
        }, 
        {
            '$group': 
            {
                '_id': None, 'avg': {'$avg': '$lenOfWeapon'}
            }
        }
    ])
    return list(result)

if __name__ == "__main__":
    mongo_client = connect_to_mongo(PASSWORD, DBNAME)
    collection = mongo_client.myFirstDatabase.myFirstDatabase
    result = weapon_each_char(collection)
    print(result)