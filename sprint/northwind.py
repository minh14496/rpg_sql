import sqlite3


expensive_items = """SELECT * FROM Product
ORDER BY UnitPrice DESC LIMIT 10;"""

avg_hire_age = "SELECT AVG(HireDate - BirthDate) FROM Employee;"

avg_age_by_city = """SELECT City, AVG(HireDate - BirthDate)
FROM Employee GROUP BY City;"""

ten_most_expensive = """SELECT ProductName, UnitPrice, CompanyName
FROM Product as p
JOIN Supplier as s
ON p.SupplierId = s.Id
ORDER BY UnitPrice DESC
LIMIT 10;"""

largest_category = """SELECT CategoryName, COUNT(DISTINCT(ProductName)) as UniqueProduct
FROM Product as p
JOIN Category as c
ON p.CategoryId = c.Id
GROUP BY CategoryName
ORDER BY UniqueProduct DESC
LIMIT 1;"""

most_territories = """SELECT e.Id, e.FirstName,e.LastName, COUNT(e.Id) as NumberTerritory
FROM Employee as e
JOIN EmployeeTerritory as et
ON e.Id = et.EmployeeId
GROUP BY e.Id
ORDER BY NumberTerritory DESC
LIMIT 1;"""

"""
    [Result]
    avg_hire_age: 37.22
    largest_category: Confections
    most_territories: King Robert 10 territories

"""


if __name__ == "__main__":
    conn = sqlite3.connect('../data/northwind_small.sqlite3')
    curs = conn.cursor()
    result = curs.execute(largest_category).fetchall()
    print(result)
