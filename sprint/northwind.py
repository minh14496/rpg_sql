import sqlite3


expensive_items = "SELECT UnitPrice FROM Product\
ORDER BY UnitPrice DESC LIMIT 10;"

avg_hire_age = "SELECT AVG(HireDate - BirthDate) FROM Employee;"

avg_age_by_city = "SELECT City, AVG(HireDate - BirthDate) \
FROM Employee GROUP BY City;"

ten_most_expensive = """SELECT ProductName, CompanyName, UnitPrice
FROM Product as p
JOIN Supplier as s
ON p.SupplierId = s.Id
ORDER BY UnitPrice DESC
LIMIT 10;"""

largest_catergory = """SELECT CategoryName, COUNT(DISTINCT(ProductName)) as UniqueProduct
FROM Product as p
JOIN Category as c
ON p.CategoryId = c.Id
GROUP BY CategoryName
ORDER BY UniqueProduct DESC
LIMIT 1;"""

"""
    [Result]

"""


if __name__ == "__main__":
    conn = sqlite3.connect('../data/northwind_small.sqlite3')
    curs = conn.cursor()