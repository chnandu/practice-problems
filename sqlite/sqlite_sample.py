#!/usr/bin/python

import sqlite3

# Specify the database file
DB_FILE = "./example.db"

# Create db connection
print("Connecting to sqlite db at %s" % DB_FILE)
conn = sqlite3.connect(DB_FILE)

# Create cursor
cur = conn.cursor()

# Create a sample table
print("Create a sample table data_store")
cur.execute("CREATE TABLE IF NOT EXISTS data_store (provider, category_id)")

# Insert a row
print("Inserting a row in to the table data_store")
cur.execute("INSERT INTO data_store VALUES ('abcd', 'crid://test')")

# Save the changes
print("Committing the changes")
conn.commit()

# Now get the data back
print("Select data from data_store")
cur.execute("SELECT * FROM data_store")
print(cur.fetchall())

try:
    cur.execute("DELETE FROM t_data_store")
except Exception as e:
    print(dir(e), e.__dict__, e.message)
cur.close()
conn.close()
