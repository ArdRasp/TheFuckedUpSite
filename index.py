#!/usr/bin/env python
# coding: utf-8

import cgi 
import random
import sqlite3

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

sqlite_connection = sqlite3.connect("./database/whoareyou.db")

cursor = sqlite_connection.cursor()
cursor.execute('SELECT * FROM data ORDER BY id LIMIT 1 OFFSET ' + str(random.randint(0, 1000)) + ';') # get the n row from the database
content = list(cursor.fetchone()) # Store the result in a list

# List of what to replace in the html file
string_ids = ["Replace That First Name", "Replace That Last Name", "Replace That email", "Replace That Phone Number", "Replace That Country"]

with open('page.html', 'r') as file: # Open html file with read permission
    data = file.read().replace('\n', '') # Remove lines break to have a string instead of a list
    for id in string_ids: # Search for the strings to replace in the html string
        data = data.replace(id, content[string_ids.index(id) + 1]) # replace them by the result of the sql command
    print(data)
    file.close()
