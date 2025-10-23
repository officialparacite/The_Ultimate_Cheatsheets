# Basic Queries

- SELECT * FROM users;                                      [//]: <> (select all columns)
- SELECT name, age FROM users;                              [//]: <> (select specific columns)
- SELECT DISTINCT city FROM users;                          [//]: <> (unique values only)
- SELECT COUNT(*) FROM users;                               [//]: <> (count rows)


# Filtering

- SELECT * FROM users                                       [//]: <> (filters based on condition)
  WHERE age > 18 AND city = 'London';

- SELECT * FROM users                                       [//]: <> (starts with A)
  WHERE name LIKE 'A%';

- SELECT * FROM users                                       [//]: <> (ends with son)
  WHERE name LIKE '%son';

- SELECT * FROM users                                       [//]: <> (contains ann)
  WHERE name LIKE '%ann%';

- SELECT * FROM users                                       [//]: <> (inclusive range)
  WHERE age BETWEEN 18 AND 30;

- SELECT * FROM users                                       [//]: <> (multiple matches)
  WHERE city IN ('Paris', 'Tokyo', 'NY');

- SELECT * FROM users                                       [//]: <> (NULL check)
  WHERE city IS NULL;


# Sorting & Limiting

- SELECT * FROM users ORDER BY age;                         [//]: <> (ORDER BY defaults to ASC)

- SELECT * FROM users ORDER BY age DESC;                    [//]: <> (ORDER BY DESC has to be explicitly mentioned)

- SELECT * FROM users ORDER BY age ASC LIMIT 5;             [//]: <> (Limits the result to 5 rows)


# Aliases

- SELECT name AS username, age AS years FROM users;         [//]: <> (sets aliases for columns and tables using the AS clause)


# Aggregation

- SELECT COUNT(*) AS total, AVG(age), MAX(age), SUM(age)    [//]: <> (performs aggregation on a selected column)
FROM users;


# GROUP BY

SELECT city, COUNT(*) AS total_users                        [//]: <> (group by non aggregated column)
FROM users
GROUP BY city;

SELECT city, AVG(age)                                       [//]: <> (HAVING filters after grouping)
FROM users
GROUP BY city
HAVING AVG(age) > 30;


# Joins 

SELECT u.name, o.id                                         [//]: <> (INNER JOIN: Joins only matching rows)
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

SELECT u.name, o.id                                         [//]: <> (LEFT JOIN: Joins matching rows from left)
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

SELECT u.name, o.id                                         [//]: <> (RIGHT JOIN: Joins matching rows from right)
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

SELECT u.name, o.id                                         [//]: <> (FULL OUTER JOIN: Joins everything from both sides)
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;


# Sub Queries

SELECT name                                                 [//]: <> (nested query is executed first before the outer query)
FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

SELECT e.name, d.dept_name                                  [//]: <> (Subqueries is super useful when using Joins)
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN (
    SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING COUNT(*) > 1
) big_depts ON e.department_id = big_depts.department_id;


# Creating a Table

CREATE TABLE people (                                       [//]: <> (Creating a table with column names followed by type of column data)
  id INTEGER, 
  tag TEXT, 
  name text, 
  age INTEGER,
  balance INTEGER,
  is_admin BOOLEAN
  );


# Renaming a Table or Column

ALTER TABLE employees                                       [//]: <> (Renaming a table to another name)
RENAME TO contractors;

ALTER TABLE contractors                                     [//]: <> (Renaming a column name inside a table)
RENAME COLUMN salary TO invoice;


# Add or Drop a column

ALTER TABLE contractors                                     [//]: <> (Add a column to an existing table)
ADD COLUMN job_title TEXT;

ALTER TABLE contractors                                     [//]: <> (Dropping a column in an existing table)
DROP COLUMN is_manager;


# Constraints

CREATE TABLE employees(
    id INTEGER PRIMARY KEY,                                 [//]: <> (The PRIMARY KEY constraint uniquely identifies each row in the table)
    name TEXT UNIQUE,                                       [//]: <> (The UNIQUE constraint ensures that no two rows can have the same value in the 'name' column)
    title TEXT NOT NULL                                     [//]: <> (The NOT NULL constraint ensures that the 'title' column cannot have NULL values)
);



