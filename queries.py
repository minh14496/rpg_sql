SELECT_CHARACTERS = "SELECT * FROM charactercreator_character;"

# total characters 302
TOTAL_CHARACTERS = "SELECT COUNT(*) FROM charactercreator_character;"

# total items 174
TOTAL_ITEMS = "SELECT COUNT(*) FROM armory_item;"

# total weapons 37
WEAPONS = "SELECT COUNT(*) FROM armory_weapon;"

# total non-weapons 137
NON_WEAPONS = "SELECT COUNT(*) \
FROM armory_item as ai \
WHERE ai.item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);"

# 302 characters with all of their items in inventory show first 20
CHARACTER_ITEMS = "SELECT character_id, COUNT(*) as item_count \
FROM charactercreator_character_inventory \
GROUP BY character_id \
LIMIT 20;"

# How many weapons does each character have show first 20
CHARACTER_WEAPONS = "SELECT character_id, COUNT(*) as weapon \
FROM charactercreator_character_inventory as cci \
INNER JOIN armory_weapon as aw \
WHERE cci.item_id = aw.item_ptr_id \
GROUP BY character_id \
LIMIT 20;"

# Using the query character_item to find the average of items each character have
AVG_CHARACTER_ITEMS = "SELECT AVG(item_count) \
FROM (SELECT character_id, COUNT(*) as item_count \
FROM charactercreator_character_inventory \
GROUP BY character_id);"

# Using the query character_weapons to find the average of weapons
# each characters have. How ever there are only 155/302 chars have 
# weapon. Thus have to left join with character table then change 
# NULL value of weapons for those don't have weapon to be 0
AVG_CHARACTER_WEAPONS = "SELECT AVG(COALESCE(weapon, 0)) \
FROM charactercreator_character as cc \
LEFT JOIN \
(SELECT character_id as char_id, COUNT(*) as weapon \
FROM charactercreator_character_inventory as cci \
INNER JOIN armory_weapon as aw \
ON cci.item_id = aw.item_ptr_id \
GROUP BY character_id) \
ON cc.character_id = char_id;"