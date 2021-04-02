import sqlite3
import FileChanges

conn = sqlite3.connect('filetrack.db')

# Create a cursor object
cursor = conn.cursor()
# Create a table
cursor.execute("create table people(id integer primary key, name text, count integer)")

# Insert a couple of records
cursor.execute("insert into people (name, count) values ('Bob', 1)")

# Confirm the inser worked
result = cursor.execute("select * from people")
print(result.fetchall())
