import pandas as pd
import sqlite3


df = pd.read_csv('data/buddymove_holidayiq.csv')
conn = sqlite3.connect('data/buddymove_holidayiq.sqlite3')
# to sql
# df.to_sql('review', conn)

if __name__ == '__main__':
    curs = conn.cursor()
    results = curs.execute("SELECT* FROM review").fetchall()
    print(df.head(20))
    curs.close()