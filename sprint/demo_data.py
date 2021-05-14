import sqlite3


demo_value = [('g', 3, 9), ('y', 5, 7), ('f', 8, 7)]

CREATE_demo = """
CREATE TABLE IF NOT EXISTS demo(
    s VARCHAR(5) NOT NULL,
    x INT NOT NULL,
    y INT NOT NULL
);"""

INSERT_demo = 'INSERT INTO demo(s, x, y) VALUES (?, ?, ?)'

# Count how many rows you have - it should be 3!
row_count = "SELECT COUNT(*) FROM demo;"

# How many rows are there where both `x` and `y` are at least 5?
xy_at_least_5 = "SELECT COUNT(*) FROM demo WHERE x >=5 AND y >=5;"

# How many unique values of `y` are there
unique_y = "SELECT COUNT(DISTINCT(y)) FROM demo;"

"""
    [Results]
    row_count is 3
    xy_at_least_5 is 2
    unique_y is 2
"""


def execute_query(conn, query, print_out=True):
    """
    Executes queries depending on if you want to commit CUD
    or to print out result
    """
    curs = conn.cursor()
    curs.execute(query)
    if print_out:
        results = curs.fetchall()
        curs.close()
        return results
    else:
        conn.commit()
        curs.close()
        return "CUD Query Executed"


if __name__ == "__main__":
    conn = sqlite3.connect('../data/demo_data.sqlite3')
    # Create demo table
    execute_query(conn, CREATE_demo, print_out=False)
    # Insert into demo table
    curs = conn.cursor()
    for value in demo_value:
        curs.execute(INSERT_demo, value)
        conn.commit()
    curs.close()
    # Testing the result
    result = execute_query(conn, unique_y)
    print(result)
