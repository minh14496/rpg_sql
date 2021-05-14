import sqlite3


demo_value = [('g',3, 9), ('y', 5, 7), ('f', 8, 7)]
CREATE_demo = """
CREATE TABLE IF NOT EXISTS demo(
    s VARCHAR(1) NOT NULL PRIMARY KEY,
    x INT NOT NULL,
    y INT NOT NULL
);"""
INSERT_demo = """
    INSERT INTO demo(
        s, x, y
    ) VALUES (
        'g', 3, 9
    );
"""


if __name__ == "__main__":
    conn = sqlite3.connect('../data/demo_data.sqlite3')
    curs = conn.cursor()
    curs.execute(CREATE_demo)
    curs.close()
    # curs = conn.cursor()
    # curs.execute(INSERT_demo)
    # conn.commit()
    # curs.close()
    curs = conn.cursor()
    # # for value in demo_value:
    # #     curs.execute(INSERT_demo, value)
    curs.execute("SELECT * FROM demo;").fetchall()
    print(list(curs))
    curs.close()
