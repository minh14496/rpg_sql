import sqlite3


# Ten most expensive items base on UnitPrice
expensive_items = """SELECT * FROM Product
ORDER BY UnitPrice DESC LIMIT 10;"""

# What is the average age of an employee at the time of their hiring?
avg_hire_age = "SELECT AVG(HireDate - BirthDate) FROM Employee;"

# How does the average age of employee at hire vary by city?
avg_age_by_city = """SELECT City, AVG(HireDate - BirthDate)
FROM Employee GROUP BY City;"""

# What are the ten most expensive items their suppliers?
ten_most_expensive = """SELECT ProductName, UnitPrice, CompanyName
FROM Product as p
JOIN Supplier as s
ON p.SupplierId = s.Id
ORDER BY UnitPrice DESC
LIMIT 10;"""

# What is the largest category (by number of unique products in it)?
largest_category = """SELECT CategoryName, COUNT(DISTINCT(ProductName)) as UniqueProduct
FROM Product as p
JOIN Category as c
ON p.CategoryId = c.Id
GROUP BY CategoryName
ORDER BY UniqueProduct DESC
LIMIT 1;"""

# Who's the employee with the most territories?
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
    # Testing the result
    result = curs.execute(largest_category).fetchall()
    print(result)
