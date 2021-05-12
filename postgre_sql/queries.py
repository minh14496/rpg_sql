# SQLite queries
EXTRACT_CHARACTERS = """
  SELECT *
  FROM charactercreator_character;
"""
EXTRACT_ITEMS = """
  SELECT *
  FROM armory_item;
"""
EXTRACT_INVENTORY = """
  SELECT *
  FROM charactercreator_character_inventory
"""
EXTRACT_WEAPON = """
  SELECT *
  FROM armory_weapon
"""
EXTRACT_MAGE = """
  SELECT *
  FROM charactercreator_mage
"""
CREATE_charactercreator_character = """
  CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
  );
"""

INSERT_INTO_charactercreator_character = """
  INSERT INTO charactercreator_character (
    name,
    level,
    exp,
    hp,
    strength,
    intelligence,
    dexterity,
    wisdom
  ) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
  );
"""
CREATE_armory_item = """
  CREATE TABLE IF NOT EXISTS armory_item (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    value INT NOT NULL,
    weight INT NOT NULL
  );
"""

INSERT_INTO_armory_item = """
  INSERT INTO armory_item (
    name,
    value,
    weight
  ) VALUES (
    %s,
    %s,
    %s
  );
"""

CREATE_charactercreator_character_inventory = """
  CREATE TABLE IF NOT EXISTS charactercreator_character_inventory (
    id SERIAL PRIMARY KEY,
    character_id INT NOT NULL,
    item_id INT NOT NULL,
    CONSTRAINT fk_character_id FOREIGN KEY (character_id)
      REFERENCES charactercreator_character (character_id),
    CONSTRAINT fk_item_id FOREIGN KEY (item_id)
      REFERENCES armory_item(item_id) 
  );
"""

INSERT_INTO_charactercreator_character_inventory = """
  INSERT INTO charactercreator_character_inventory (
    id,
    character_id,
    item_id
  ) VALUES (
    %s,
    %s,
    %s
  );
"""

CREATE_armory_weapon = """
  CREATE TABLE IF NOT EXISTS armory_weapon (
    item_ptr_id INT NOT NULL,
    power INT NOT NULL,
    CONSTRAINT pk_item_ptr_id PRIMARY KEY (item_ptr_id),
    CONSTRAINT fk_item_ptr_id FOREIGN KEY(item_ptr_id)
      REFERENCES armory_item(item_id)
  );
"""

INSERT_INTO_armory_weapon = """
  INSERT INTO armory_weapon (
    item_ptr_id,
    power
  ) VALUES (
    %s,
    %s
  );
"""

CREATE_charactercreator_mage = """
  CREATE TABLE IF NOT EXISTS charactercreator_mage (
    character_ptr_id INT NOT NULL,
    has_pet INT NOT NULL,
    mana INT NOT NULL,
    CONSTRAINT pk_character_ptr_id PRIMARY KEY (character_ptr_id),
    CONSTRAINT fk_character_ptr_id FOREIGN KEY(character_ptr_id)
      REFERENCES charactercreator_character(character_id)
  );
"""

INSERT_INTO_charactercreator_mage = """
  INSERT INTO charactercreator_mage (
    character_ptr_id,
    has_pet,
    mana
  ) VALUES (
    %s,
    %s,
    %s
  );
"""
### Titanic ###
EXTRACT_TITANIC ="""
  SELECT *
  FROM titanic
"""

CREATE_titanic = """
  CREATE TABLE IF NOT EXISTS titanic (
    Index SERIAL PRIMARY KEY,
    Survived INT NOT NULL,
    Pclass INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Sex VARCHAR(30) NOT NULL, 
    Age INT NOT NULL,
    Siblings_Spouses_Aboard INT NOT NULL,
    Parents_Children_Aboard INT NOT NULL, 
    Fare FLOAT NOT NULL
  );
"""

COPY_titanic = """
  COPY titanic(Survived, Pclass, Name, Sex, Age, 
  Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
  FROM '../data/titanic.csv'
  DELIMITER ','
  CSV;
"""

INSERT_INTO_titanic = """
  INSERT INTO titanic(
    Index,
    Survived, 
    Pclass, 
    Name, 
    Sex, 
    Age,
    Siblings_Spouses_Aboard, 
    Parents_Children_Aboard, 
    Fare
  ) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
  );
"""


# For Postgresl_example.py
SQL_CREATE_TABLE = """
  CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    age INT
  );
"""

SQL_INSERT_DATA = """
  INSERT INTO test_table (
    name,
    age
  ) VALUES (
    'Carl',
    102
  );
"""

SQL_SHOW_TABLE = """
  SELECT * FROM test_table;
"""