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
    result = total_item_in_inventory(collection)
    print(result)


# How many passengers survived, and how many died?
PASSENGER_SURVIVED = """SELECT survived, COUNT(*) 
FROM titanic
GROUP BY survived;"""

# How many passengers were in each class?
PASSENGER_IN_CLASS = """SELECT pclass, COUNT(*) 
FROM titanic
GROUP BY pclass;"""

# How many passengers survived/died within each class?
PASSENGER_SURVIVED_EACH_CLASS = """SELECT survived, pclass, COUNT(*) 
FROM titanic
GROUP BY pclass, survived
ORDER BY survived;"""

# What was the average age of survivors vs nonsurvivors?
AVERAGE_AGE_SURVIVOR = """SELECT survived, AVG(age) 
FROM titanic
GROUP BY survived;"""

# What was the average age of each passenger class?
AVERAGE_AGE_PCLASS = """SELECT pclass, AVG(age) 
FROM titanic
GROUP BY pclass;"""

# What was the average fare by passenger class? By survival?
AVERAGE_FARE_BY_CLASS_SURVIVED = """SELECT survived, pclass, AVG(fare) 
FROM titanic
GROUP BY survived, pclass;"""

# How many siblings/spouses aboard on average, by passenger class? By survival?
AVERAGE_SIBLINGS_CLASS_SURVIVED = """SELECT survived, pclass, AVG(siblings_spouses_aboard) 
FROM titanic
GROUP BY survived, pclass;"""

# How many parents/children aboard on average, by passenger class? By survival?
AVERAGE_PARENTS_CLASS_SURVIVED = """SELECT survived, pclass, AVG(parents_children_aboard) 
FROM titanic
GROUP BY survived, pclass;"""

# Do any passengers have the same name? No row return means that every name different
ANY_NAME_THE_SAME = """SELECT name, COUNT(*)
FROM titanic
GROUP BY name
HAVING COUNT(*)>1;"""

#How many marriedcouples were aboard the Titanic? Assume that two people 
# (one `Mr.` and one`Mrs.`) with the same last name and with at least 
# 1 sibling/spouse aboard are a married couple.

MARRIED_COUPLES = """
"""