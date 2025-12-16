
---

## Starting SQLite

```sh
sqlite3 test.db			# open (or create) database
sqlite3 :memory:		# in-memory database
```
## Starting SQLite in Neovim using vim-dadbod plugin

```sh
:DBUI					# starts the dadbod UI
:sqlite:/<file_path>	# add database to the list 
```

## Meta / Dot Commands (sqlite3 shell only)

```sql
.help				-- show help
.tables				-- list tables
.schema				-- show schema of all tables
.schema users			-- show schema of specific table
.databases			-- list attached databases
.headers on			-- show column headers
.mode column			-- pretty column output
.mode csv			-- CSV output
.output file.csv		-- redirect output to file
.quit				-- exit sqlite3
```

## Creating Tables

```sql
CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	age INTEGER,
	email TEXT UNIQUE
);
```

## Data Types (SQLite is dynamically typed)

```text
INTEGER
REAL
TEXT
BLOB
NULL
```

## Insert Data

```sql
INSERT INTO users (name, age, email)
VALUES ('Alice', 25, 'alice@mail.com');

INSERT INTO users VALUES (NULL, 'Bob', 30, 'bob@mail.com');
```

## Select Queries

```sql
SELECT * FROM users;
SELECT name, age FROM users;
SELECT DISTINCT age FROM users;
```

## WHERE Conditions

```sql
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE name = 'Alice';
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
SELECT * FROM users WHERE email IS NULL;
```

## Logical Operators

```sql
SELECT * FROM users WHERE age > 20 AND age < 40;
SELECT * FROM users WHERE name = 'Alice' OR name = 'Bob';
SELECT * FROM users WHERE NOT age = 30;
```

## LIKE / Pattern Matching

```sql
SELECT * FROM users WHERE name LIKE 'A%';	-- starts with A
SELECT * FROM users WHERE email LIKE '%@mail.com';
SELECT * FROM users WHERE name LIKE '_l%';	-- single char wildcard
```

## Ordering & Limiting

```sql
SELECT * FROM users ORDER BY age ASC;
SELECT * FROM users ORDER BY age DESC;
SELECT * FROM users LIMIT 5;
SELECT * FROM users LIMIT 5 OFFSET 10;
```

## Update Data

```sql
UPDATE users SET age = 26 WHERE name = 'Alice';
UPDATE users SET email = NULL;
```

## Delete Data

```sql
DELETE FROM users WHERE name = 'Bob';
DELETE FROM users;		-- delete all rows
```

## Aggregate Functions

```sql
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
SELECT MIN(age), MAX(age) FROM users;
SELECT SUM(age) FROM users;
```

## GROUP BY / HAVING

```sql
SELECT age, COUNT(*)
FROM users
GROUP BY age;

SELECT age, COUNT(*)
FROM users
GROUP BY age
HAVING COUNT(*) > 1;
```

## Joins

```sql
SELECT u.name, o.amount
FROM users u
JOIN orders o ON u.id = o.user_id;

SELECT *
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

## Indexes

```sql
CREATE INDEX idx_users_age ON users(age);
DROP INDEX idx_users_age;
```

## Constraints

```sql
PRIMARY KEY
UNIQUE
NOT NULL
DEFAULT 0
CHECK(age >= 0)
```

## Alter Table (limited support)

```sql
ALTER TABLE users ADD COLUMN city TEXT;
```

## Transactions

```sql
BEGIN;
INSERT INTO users VALUES (NULL, 'Eve', 22, NULL);
COMMIT;

ROLLBACK;
```

## Foreign Keys

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE orders (
	id INTEGER PRIMARY KEY,
	user_id INTEGER,
	amount REAL,
	FOREIGN KEY(user_id) REFERENCES users(id)
);
```

## Import / Export

```sh
sqlite3 db.sqlite < dump.sql
```

```sql
.mode csv
.import data.csv users
```

```sql
.headers on
.mode csv
.output out.csv
SELECT * FROM users;
.output stdout
```

## Backup / Dump

```sh
sqlite3 db.sqlite .dump > dump.sql
```

## Useful PRAGMAs

```sql
PRAGMA table_info(users);	-- column info
PRAGMA database_list;
PRAGMA journal_mode;
PRAGMA integrity_check;
```

## Exit Codes (CLI)

```sh
sqlite3 db.sqlite "SELECT 1;" || echo "failed"
```

---

## Constraints (Detailed)

### Column-level Constraints

```sql
id INTEGER PRIMARY KEY
name TEXT NOT NULL
email TEXT UNIQUE
age INTEGER DEFAULT 18
score INTEGER CHECK(score >= 0)
```

### Table-level Constraints

```sql
CREATE TABLE users (
	id INTEGER,
	email TEXT,
	age INTEGER,
	PRIMARY KEY (id),
	UNIQUE (email),
	CHECK (age >= 0)
);
```

### Foreign Key Constraints

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE orders (
	id INTEGER PRIMARY KEY,
	user_id INTEGER,
	amount REAL,
	FOREIGN KEY (user_id)
		REFERENCES users(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);
```

### Constraint Actions

```text
ON DELETE CASCADE
ON DELETE SET NULL
ON DELETE RESTRICT
ON UPDATE CASCADE
```

---

## Subqueries

### Subquery in WHERE

```sql
SELECT name
FROM users
WHERE id IN (
	SELECT user_id FROM orders
);
```

### Subquery with Comparison

```sql
SELECT name
FROM users
WHERE age > (
	SELECT AVG(age) FROM users
);
```

### Subquery with EXISTS

```sql
SELECT name
FROM users u
WHERE EXISTS (
	SELECT 1
	FROM orders o
	WHERE o.user_id = u.id
);
```

### Subquery in SELECT

```sql
SELECT
	name,
	(SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;
```

### Subquery in FROM (Derived Table)

```sql
SELECT avg_age
FROM (
	SELECT AVG(age) AS avg_age FROM users
);
```

---

## Correlated Subqueries

(Subquery depends on outer query row)

```sql
SELECT name
FROM users u
WHERE age > (
	SELECT AVG(age)
	FROM users
	WHERE city = u.city
);
```

---

## Common Subquery Operators

```sql
IN
NOT IN
EXISTS
NOT EXISTS
ANY
ALL
```

Example:

```sql
SELECT name
FROM users
WHERE age >= ALL (
	SELECT age FROM users WHERE city = 'Delhi'
);
```

---

## Constraint Introspection

```sql
PRAGMA table_info(users);	-- columns + constraints
PRAGMA foreign_key_list(orders);
```

---
