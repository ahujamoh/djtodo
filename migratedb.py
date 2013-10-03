#!/usr/bin/env python
"""
Script to migrate data from 
one sqlite database table which has the structure as:
|  id  |  title  |  description  |  datetime  |
to one sqlite database table which should have structure as:
|  id  |  title  |  datetime  |  priority  |  status  |
"""

import sqlite3

conn1 = sqlite3.connect('data.db')
c1 = conn1.cursor()

conn2 = sqlite3.connect('newdata.db')
c2 = conn2.cursor()

# Creating the database tabls if not exist
c2.execute(
            """
               CREATE TABLE IF NOT EXISTS todoapp_TodoList
    (id, title, datetime, priority, status)
    """)

print "Data migration started"

# Migration loop
for row in c1.execute('SELECT * FROM todoapp_TodoList'):
    no, title, desc, datetime = row
    c2.execute(
               """
               INSERT INTO todoapp_TodoList
    (id, title, datetime, priority, status)
    values (?, ?, ?, ?, ?);
    """, (no, title, datetime, "", "")
    )

conn2.commit()
conn2.close()
print "Migration completed successfully"
