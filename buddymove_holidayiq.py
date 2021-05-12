import pandas as pd
import sqlite3


df = pd.read_csv('data/buddymove_holidayiq.csv')
conn = sqlite3.connect('data/buddymove_holidayiq.sqlite3')
queries = {
    'count': "SELECT COUNT(*) FROM review",
    'nature_shopping': "SELECT COUNT(*) \
    FROM review \
    WHERE Nature > 100 and Shopping > 100;",
    'average_col': "SELECT AVG(Sports), AVG(Religious), \
    AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic) \
    FROM review;"
    }
df.to_sql('review', conn)

if __name__ == '__main__':
    curs = conn.cursor()
    results = curs.execute(queries['count']).fetchall()
    print(results)
    curs.close()