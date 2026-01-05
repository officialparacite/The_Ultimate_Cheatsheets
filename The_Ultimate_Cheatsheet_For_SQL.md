
---

# SQLite Database

---

## Index

| * | Table of Contents |
|---|-------------------|
| - | [Starting SQLite](#starting-sqlite) |
| - | [Meta / Dot Commands](#meta--dot-commands) |
| - | [Data Types](#data-types) |
| - | [Creating Tables](#creating-tables) |
| - | [Insert Data](#insert-data) |
| - | [Select Queries](#select-queries) |
| - | [WHERE Conditions](#where-conditions) |
| - | [Logical Operators](#logical-operators) |
| - | [LIKE / Pattern Matching](#like--pattern-matching) |
| - | [Ordering & Limiting](#ordering--limiting) |
| - | [Update Data](#update-data) |
| - | [Delete Data](#delete-data) |
| - | [Aggregate Functions](#aggregate-functions) |
| - | [GROUP BY / HAVING](#group-by--having) |
| - | [Joins](#joins) |
| - | [Subqueries](#subqueries) |
| - | [Indexes](#indexes) |
| - | [Constraints](#constraints) |
| - | [Alter Table](#alter-table) |
| - | [Transactions](#transactions) |
| - | [Foreign Keys](#foreign-keys) |
| - | [Views](#views) |
| - | [Import / Export](#import--export) |
| - | [Backup / Dump](#backup--dump) |
| - | [Useful PRAGMAs](#useful-pragmas) |

---

## Starting SQLite

```sh
sqlite3 test.db                     # open (or create) database
sqlite3 :memory:                    # in-memory database
sqlite3 test.db "SELECT * FROM t"   # run query directly
sqlite3 -header -column test.db     # with formatting options
```

### Starting SQLite in Neovim (vim-dadbod)

```sh
:DBUI                               # starts the dadbod UI
:sqlite:/<file_path>                # add database to the list
```

---

## Meta / Dot Commands

> [!NOTE]
> These commands work only in the sqlite3 shell, not in SQL files.

### Help & Info

```sql
.help                               -- show help
.tables                             -- list all tables
.schema                             -- show schema of all tables
.schema users                       -- show schema of specific table
.databases                          -- list attached databases
```

### Output Formatting

```sql
.headers on                         -- show column headers
.headers off                        -- hide column headers
.mode column                        -- pretty column output
.mode csv                           -- CSV output
.mode json                          -- JSON output
.mode table                         -- ASCII table output
.mode line                          -- one value per line
.width 15 10 20                     -- set column widths
```

### Output Redirection

```sql
.output file.txt                    -- redirect output to file
.output stdout                      -- reset to standard output
.once file.txt                      -- output only next command to file
```

### Session Control

```sql
.quit                               -- exit sqlite3
.exit                               -- exit sqlite3
```

---

## Data Types

SQLite uses dynamic typing with 5 storage classes:

| Type | Description |
|------|-------------|
| `INTEGER` | Signed integer (1, 2, 3, 4, 6, or 8 bytes) |
| `REAL` | Floating point (8-byte IEEE) |
| `TEXT` | Text string (UTF-8, UTF-16) |
| `BLOB` | Binary data |
| `NULL` | Null value |

### Type Affinity

```sql
-- SQLite converts declared types to affinity:
INT, INTEGER, TINYINT, SMALLINT, BIGINT    → INTEGER
REAL, DOUBLE, FLOAT                         → REAL
CHAR, VARCHAR, TEXT, CLOB                   → TEXT
BLOB                                        → BLOB
-- Anything else                            → NUMERIC
```

---

## Creating Tables

### Basic Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
);
```

### Create If Not Exists

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
);
```

### Create from Select

```sql
CREATE TABLE users_backup AS
SELECT * FROM users;
```

### Temporary Table

```sql
CREATE TEMP TABLE temp_data (
    id INTEGER,
    value TEXT
);
```

### Drop Table

```sql
DROP TABLE users;
DROP TABLE IF EXISTS users;
```

---

## Insert Data

### Basic Insert

```sql
INSERT INTO users (name, age, email)
VALUES ('Alice', 25, 'alice@mail.com');
```

### Insert All Columns

```sql
-- NULL for AUTOINCREMENT column
INSERT INTO users VALUES (NULL, 'Bob', 30, 'bob@mail.com');
```

### Insert Multiple Rows

```sql
INSERT INTO users (name, age) VALUES
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 35);
```

### Insert from Select

```sql
INSERT INTO users_backup
SELECT * FROM users WHERE age > 25;
```

### Insert or Replace

```sql
INSERT OR REPLACE INTO users (id, name, age)
VALUES (1, 'Alice', 26);

-- Shorthand
REPLACE INTO users (id, name, age)
VALUES (1, 'Alice', 26);
```

### Insert or Ignore

```sql
INSERT OR IGNORE INTO users (id, name)
VALUES (1, 'Alice');                    -- ignores if id exists
```

---

## Select Queries

### Basic Select

```sql
SELECT * FROM users;                    -- all columns
SELECT name, age FROM users;            -- specific columns
SELECT DISTINCT age FROM users;         -- unique values
```

### Column Aliases

```sql
SELECT name AS username, age AS years
FROM users;

SELECT name username, age years         -- AS is optional
FROM users;
```

### Expressions

```sql
SELECT name, age * 12 AS age_months FROM users;
SELECT name || ' (' || age || ')' AS display FROM users;
```

### Table Aliases

```sql
SELECT u.name, u.age
FROM users u;
```

---

## WHERE Conditions

### Comparison Operators

```sql
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE age >= 25;
SELECT * FROM users WHERE age < 30;
SELECT * FROM users WHERE age <= 30;
SELECT * FROM users WHERE age = 25;
SELECT * FROM users WHERE age != 25;
SELECT * FROM users WHERE age <> 25;    -- same as !=
```

### BETWEEN

```sql
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
SELECT * FROM users WHERE age NOT BETWEEN 20 AND 30;
```

### IN

```sql
SELECT * FROM users WHERE age IN (20, 25, 30);
SELECT * FROM users WHERE name IN ('Alice', 'Bob');
SELECT * FROM users WHERE age NOT IN (20, 25, 30);
```

### NULL Checks

```sql
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

### String Comparison

```sql
SELECT * FROM users WHERE name = 'Alice';
SELECT * FROM users WHERE name LIKE 'A%';
```

---

## Logical Operators

```sql
-- AND: both conditions must be true
SELECT * FROM users WHERE age > 20 AND age < 40;

-- OR: at least one condition must be true
SELECT * FROM users WHERE name = 'Alice' OR name = 'Bob';

-- NOT: negate condition
SELECT * FROM users WHERE NOT age = 30;
SELECT * FROM users WHERE NOT (age > 20 AND age < 30);

-- Combined
SELECT * FROM users
WHERE (age > 20 AND age < 30)
   OR name = 'Admin';
```

---

## LIKE / Pattern Matching

```sql
-- % = any sequence of characters (including empty)
SELECT * FROM users WHERE name LIKE 'A%';           -- starts with A
SELECT * FROM users WHERE name LIKE '%son';         -- ends with son
SELECT * FROM users WHERE email LIKE '%@mail.com';  -- contains @mail.com
SELECT * FROM users WHERE name LIKE '%li%';         -- contains li

-- _ = exactly one character
SELECT * FROM users WHERE name LIKE '_lice';        -- ?lice (Alice, Blice, etc.)
SELECT * FROM users WHERE name LIKE 'A___';         -- A followed by 3 chars

-- Case insensitive by default
-- Use GLOB for case-sensitive matching
SELECT * FROM users WHERE name GLOB 'A*';           -- case-sensitive

-- ESCAPE character
SELECT * FROM products WHERE name LIKE '%10\%%' ESCAPE '\';  -- contains 10%
```

---

## Ordering & Limiting

### ORDER BY

```sql
SELECT * FROM users ORDER BY age;                   -- ascending (default)
SELECT * FROM users ORDER BY age ASC;               -- ascending
SELECT * FROM users ORDER BY age DESC;              -- descending
SELECT * FROM users ORDER BY age DESC, name ASC;    -- multiple columns
SELECT * FROM users ORDER BY 2;                     -- by column position
```

### LIMIT

```sql
SELECT * FROM users LIMIT 5;                        -- first 5 rows
SELECT * FROM users LIMIT 5 OFFSET 10;              -- 5 rows, skip first 10
SELECT * FROM users LIMIT 10, 5;                    -- same as above (offset, limit)
```

### Combined

```sql
SELECT * FROM users
ORDER BY age DESC
LIMIT 3;                                            -- top 3 oldest
```

---

## Update Data

### Basic Update

```sql
UPDATE users SET age = 26 WHERE name = 'Alice';
```

### Update Multiple Columns

```sql
UPDATE users
SET age = 26, email = 'alice@new.com'
WHERE name = 'Alice';
```

### Update All Rows

```sql
UPDATE users SET status = 'active';                 -- updates ALL rows
```

### Update with Expression

```sql
UPDATE users SET age = age + 1;                     -- increment all ages
UPDATE products SET price = price * 1.1;            -- 10% increase
```

### Update with Subquery

```sql
UPDATE users
SET category = (SELECT name FROM categories WHERE id = users.cat_id);
```

---

## Delete Data

### Delete with Condition

```sql
DELETE FROM users WHERE name = 'Bob';
DELETE FROM users WHERE age < 18;
```

### Delete All Rows

```sql
DELETE FROM users;                                  -- delete all (keeps table)
```

### Truncate (faster for large tables)

```sql
-- SQLite doesn't have TRUNCATE, use:
DELETE FROM users;
VACUUM;                                             -- reclaim space
```

---

## Aggregate Functions

```sql
SELECT COUNT(*) FROM users;                         -- count all rows
SELECT COUNT(email) FROM users;                     -- count non-NULL emails
SELECT COUNT(DISTINCT age) FROM users;              -- count unique ages

SELECT AVG(age) FROM users;                         -- average
SELECT SUM(age) FROM users;                         -- sum
SELECT MIN(age) FROM users;                         -- minimum
SELECT MAX(age) FROM users;                         -- maximum

SELECT MIN(age), MAX(age), AVG(age) FROM users;     -- combined

-- String aggregation
SELECT GROUP_CONCAT(name) FROM users;               -- Alice,Bob,Charlie
SELECT GROUP_CONCAT(name, ' | ') FROM users;        -- Alice | Bob | Charlie
```

---

## GROUP BY / HAVING

### Basic GROUP BY

```sql
SELECT age, COUNT(*) AS count
FROM users
GROUP BY age;
```

### Multiple Columns

```sql
SELECT city, age, COUNT(*)
FROM users
GROUP BY city, age;
```

### HAVING (filter groups)

```sql
SELECT age, COUNT(*) AS count
FROM users
GROUP BY age
HAVING COUNT(*) > 1;                                -- only groups with > 1

SELECT age, COUNT(*) AS count
FROM users
GROUP BY age
HAVING count > 1;                                   -- can use alias
```

### Complete Query Order

```sql
SELECT city, AVG(age) AS avg_age
FROM users
WHERE status = 'active'                             -- filter rows first
GROUP BY city                                       -- then group
HAVING AVG(age) > 25                                -- filter groups
ORDER BY avg_age DESC                               -- sort results
LIMIT 10;                                           -- limit output
```

---

## Joins

### INNER JOIN

```sql
SELECT users.name, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Using aliases
SELECT u.name, o.amount
FROM users u
JOIN orders o ON u.id = o.user_id;                  -- JOIN = INNER JOIN
```

### LEFT JOIN

```sql
SELECT u.name, o.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;             -- all users, matching orders
```

### Multiple Joins

```sql
SELECT u.name, o.amount, p.name AS product
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN products p ON o.product_id = p.id;
```

### Self Join

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

### Cross Join

```sql
SELECT * FROM colors CROSS JOIN sizes;              -- cartesian product
SELECT * FROM colors, sizes;                        -- same thing
```

### Natural Join (matches common columns)

```sql
SELECT * FROM users NATURAL JOIN orders;            -- joins on same column names
```

---

## Subqueries

### Subquery in WHERE

```sql
SELECT name FROM users
WHERE id IN (
    SELECT user_id FROM orders
);

SELECT name FROM users
WHERE id NOT IN (
    SELECT user_id FROM orders WHERE amount < 100
);
```

### Subquery with Comparison

```sql
SELECT name FROM users
WHERE age > (
    SELECT AVG(age) FROM users
);
```

### Subquery with EXISTS

```sql
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.user_id = u.id
);

SELECT name FROM users u
WHERE NOT EXISTS (
    SELECT 1 FROM orders o
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
) AS subquery;
```

### Correlated Subquery

```sql
-- Subquery depends on outer query row
SELECT name FROM users u
WHERE age > (
    SELECT AVG(age) FROM users
    WHERE city = u.city
);
```

### Subquery Operators

```sql
-- IN / NOT IN
WHERE id IN (SELECT ...)

-- EXISTS / NOT EXISTS
WHERE EXISTS (SELECT ...)

-- Comparison with ANY/ALL
WHERE age > ALL (SELECT age FROM users WHERE city = 'Delhi')
WHERE age > ANY (SELECT age FROM users WHERE city = 'Delhi')
```

---

## Indexes

### Create Index

```sql
CREATE INDEX idx_users_age ON users(age);
CREATE INDEX idx_users_name_age ON users(name, age);    -- composite index
```

### Unique Index

```sql
CREATE UNIQUE INDEX idx_users_email ON users(email);
```

### Create If Not Exists

```sql
CREATE INDEX IF NOT EXISTS idx_users_age ON users(age);
```

### Drop Index

```sql
DROP INDEX idx_users_age;
DROP INDEX IF EXISTS idx_users_age;
```

### List Indexes

```sql
.indexes                                            -- all indexes
.indexes users                                      -- indexes on users table
SELECT * FROM sqlite_master WHERE type = 'index';
```

---

## Constraints

### Column Constraints

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,                         -- primary key
    id INTEGER PRIMARY KEY AUTOINCREMENT,           -- auto-increment
    name TEXT NOT NULL,                             -- required
    email TEXT UNIQUE,                              -- unique values
    age INTEGER DEFAULT 18,                         -- default value
    score INTEGER CHECK(score >= 0),                -- validation
    status TEXT DEFAULT 'active' NOT NULL           -- combined
);
```

### Table Constraints

```sql
CREATE TABLE users (
    id INTEGER,
    email TEXT,
    age INTEGER,
    PRIMARY KEY (id),
    UNIQUE (email),
    CHECK (age >= 0 AND age <= 150)
);
```

### Composite Primary Key

```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

### Constraint Summary

| Constraint | Description |
|------------|-------------|
| `PRIMARY KEY` | Unique identifier |
| `AUTOINCREMENT` | Auto-generate ID |
| `NOT NULL` | Disallow NULL |
| `UNIQUE` | Unique values |
| `DEFAULT value` | Default value |
| `CHECK(expr)` | Validation rule |
| `FOREIGN KEY` | Reference other table |

---

## Alter Table

> [!NOTE]
> SQLite has limited ALTER TABLE support.

### Add Column

```sql
ALTER TABLE users ADD COLUMN city TEXT;
ALTER TABLE users ADD COLUMN created_at TEXT DEFAULT CURRENT_TIMESTAMP;
```

### Rename Table

```sql
ALTER TABLE users RENAME TO customers;
```

### Rename Column (SQLite 3.25+)

```sql
ALTER TABLE users RENAME COLUMN name TO username;
```

### Drop Column (SQLite 3.35+)

```sql
ALTER TABLE users DROP COLUMN city;
```

### Workaround for Unsupported Operations

```sql
-- For complex changes, recreate the table:
BEGIN TRANSACTION;

CREATE TABLE users_new (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
    -- modified schema
);

INSERT INTO users_new SELECT id, name FROM users;

DROP TABLE users;

ALTER TABLE users_new RENAME TO users;

COMMIT;
```

---

## Transactions

### Basic Transaction

```sql
BEGIN TRANSACTION;                                  -- or just BEGIN
INSERT INTO users VALUES (NULL, 'Eve', 22, NULL);
INSERT INTO users VALUES (NULL, 'Frank', 28, NULL);
COMMIT;
```

### Rollback

```sql
BEGIN;
UPDATE users SET age = 0;
-- Oops, wrong update!
ROLLBACK;                                           -- undo changes
```

### Savepoints

```sql
BEGIN;
INSERT INTO users (name) VALUES ('Alice');
SAVEPOINT sp1;
INSERT INTO users (name) VALUES ('Bob');
ROLLBACK TO sp1;                                    -- undo Bob, keep Alice
COMMIT;
```

### Transaction Modes

```sql
BEGIN DEFERRED;                                     -- default, lock on first access
BEGIN IMMEDIATE;                                    -- lock immediately for write
BEGIN EXCLUSIVE;                                    -- exclusive lock
```

---

## Foreign Keys

### Enable Foreign Keys

```sql
PRAGMA foreign_keys = ON;                           -- must enable (off by default)
```

### Create Foreign Key

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### With Actions

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

### Foreign Key Actions

| Action | Description |
|--------|-------------|
| `CASCADE` | Delete/update related rows |
| `SET NULL` | Set to NULL |
| `SET DEFAULT` | Set to default value |
| `RESTRICT` | Prevent delete/update |
| `NO ACTION` | Same as RESTRICT (default) |

### Check Foreign Keys

```sql
PRAGMA foreign_key_list(orders);                    -- list FKs on table
PRAGMA foreign_key_check;                           -- check for violations
```

---

## Views

### Create View

```sql
CREATE VIEW active_users AS
SELECT * FROM users WHERE status = 'active';
```

### Create or Replace

```sql
-- SQLite doesn't support CREATE OR REPLACE, use:
DROP VIEW IF EXISTS active_users;
CREATE VIEW active_users AS
SELECT * FROM users WHERE status = 'active';
```

### Query View

```sql
SELECT * FROM active_users;
SELECT name FROM active_users WHERE age > 25;
```

### Drop View

```sql
DROP VIEW active_users;
DROP VIEW IF EXISTS active_users;
```

### List Views

```sql
SELECT name FROM sqlite_master WHERE type = 'view';
```

---

## Import / Export

### Import CSV

```sql
.mode csv
.import data.csv users                              -- import into existing table

-- With headers
.mode csv
.headers on
.import --skip 1 data.csv users                     -- skip header row
```

### Export CSV

```sql
.headers on
.mode csv
.output users.csv
SELECT * FROM users;
.output stdout                                      -- reset output
```

### Export JSON

```sql
.mode json
.output users.json
SELECT * FROM users;
.output stdout
```

### Run SQL File

```sh
sqlite3 test.db < script.sql
sqlite3 test.db ".read script.sql"
```

---

## Backup / Dump

### Dump Entire Database

```sh
sqlite3 test.db .dump > backup.sql
```

### Dump Specific Table

```sh
sqlite3 test.db ".dump users" > users_backup.sql
```

### Restore from Dump

```sh
sqlite3 new.db < backup.sql
```

### Backup Command (binary copy)

```sql
.backup main backup.db
.backup backup.db                                   -- shorthand
```

### Restore from Backup

```sql
.restore main backup.db
```

---

## Useful PRAGMAs

### Table Information

```sql
PRAGMA table_info(users);                           -- column info
PRAGMA table_list;                                  -- list all tables
PRAGMA foreign_key_list(orders);                    -- foreign keys
PRAGMA index_list(users);                           -- indexes on table
```

### Database Information

```sql
PRAGMA database_list;                               -- attached databases
PRAGMA schema_version;                              -- schema version number
PRAGMA user_version;                                -- user-defined version
PRAGMA page_count;                                  -- number of pages
PRAGMA page_size;                                   -- page size in bytes
```

### Settings

```sql
PRAGMA foreign_keys = ON;                           -- enable foreign keys
PRAGMA case_sensitive_like = ON;                    -- case-sensitive LIKE
PRAGMA journal_mode = WAL;                          -- write-ahead logging
```

### Maintenance

```sql
PRAGMA integrity_check;                             -- check database integrity
PRAGMA quick_check;                                 -- faster integrity check
PRAGMA optimize;                                    -- optimize database
VACUUM;                                             -- rebuild database, reclaim space
```

### Common PRAGMA Summary

| PRAGMA | Description |
|--------|-------------|
| `table_info(t)` | Column details |
| `foreign_key_list(t)` | Foreign keys |
| `index_list(t)` | Indexes on table |
| `foreign_keys = ON` | Enable FK enforcement |
| `journal_mode` | Transaction journal mode |
| `integrity_check` | Verify database |
| `VACUUM` | Rebuild and compact |

---

[↑ Back to Index](#index)
