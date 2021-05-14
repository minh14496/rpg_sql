import sqlite3


demo_value = [('g', 3, 9), ('y', 5, 7), ('f', 8, 7)]

CREATE_demo = """
CREATE TABLE IF NOT EXISTS demo(
    s VARCHAR(5) NOT NULL,
    x INT NOT NULL,
    y INT NOT NULL
);"""

row_count = "SELECT COUNT(*) FROM demo;"

xy_at_least_5 = "SELECT COUNT(*) FROM demo WHERE x >=5 AND y >=5;"

unique_y = "SELECT COUNT(DISTINCT(y)) FROM demo;"

"""
    row_count is 3
    xy_at_least_5 is 2
    unique_y is 2
"""

if __name__ == "__main__":
    conn = sqlite3.connect('../data/demo_data.sqlite3')
    curs = conn.cursor()
    curs.execute(CREATE_demo)
    curs.close()
    curs = conn.cursor()
    for value in demo_value:
        curs.execute('INSERT INTO demo(s, x, y) VALUES (?, ?, ?)', value)
        conn.commit()
    curs.close()
    # Testing the result
    curs = conn.cursor()
    result = curs.execute(row_count).fetchall()
    print(result)
