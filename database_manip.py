# I got help from my friends Mpho and Andile.
# I got some guidelines from https://docs.python.org/3/library/sqlite3.html

#  Import sqlite3.
import sqlite3

# Creates or opens a file called python_programming with a SQLite3 DB.
# Get a cursor object.
db = sqlite3.connect("test.db")
cur = db.cursor()


# Create a table called python_programming.
cur.execute("DROP TABLE IF EXISTS python_programming")
Table = ''' CREATE TABLE python_programming (
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            grade INT
        ); '''

# Insert the following new rows into the python_programming table.
cur.execute(Table)
data = [
    (55, 'Carl Devis', 61),
    (66, 'Denis Fredrickson', 88),
    (77, 'Jane Riachards', 78),
    (12, 'Peyton Swayer', 45),
    (2, 'Lucas Brooke', 99)
]
# Execute many rows in the table.
# Remember to commit the transaction after executing INSERT.
cur.executemany('INSERT INTO python_programming VALUES(?, ?, ?)', data)
db.commit()


# Query 1: Select all records with a grade between 60 and 80.
print('\nQuery 1......')
for row in cur.execute("SELECT * FROM python_programming WHERE grade >= 60 and grade <= 80;"):
    print(row)


# Query 2: Change Carl Davis’s grade to 65.
# Update Carl Davis's grade.
print('\nQuery 2......')
cur.execute('UPDATE python_programming SET grade = 65 WHERE name="Carl Devis";')
for row in cur.execute('SELECT * FROM python_programming;'):
    print(row)


# Query 3: Delete Dennis Fredrickson’s row.
# Delete Dennis Fredrickson's entire row.
print('\nQuery 3.......')
cur.execute('DELETE FROM python_programming WHERE name="Denis Fredrickson";')
for row in cur.execute('SELECT * FROM python_programming;'):
    print(row)


# Query 4: Change the grade of all people with an id below than 55.
# Change grade of all people with id below 55 (and I set grade to 10 as my choice).
print('\nQuery 4.......')
cur.execute('UPDATE python_programming SET grade = 10 WHERE id < 55;')
for row in cur.execute('SELECT * FROM python_programming;'):
    print(row)

# Remember to commit the transaction after executing INSERT.
# We need to close the database connection.
db.commit()
db.close()
print('Connection to database closed')
