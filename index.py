#!/bin/python3.9
# coding: utf-8

import cgi 
import psycopg2
import random

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

postgres_connect = psycopg2.connect ( # Connecting to the database
    host="localhost",
    port="5432",
    dbname="whoareyou",
    user="postgres",
    password="passwd",
)

cursor = postgres_connect.cursor() # intialize the cursor 
cursor.execute(f'SELECT * FROM data OFFSET {random.randint(0, 1000)} LIMIT 1') # get the n row from the database
content = list(cursor.fetchone()) # Store the result in a list

# List of what to replace in the html file
string_ids = ["Replace That First Name", "Replace That Last Name", "Replace That email", "Replace That Phone Number", "Replace That Country"]

with open('page.html', 'r') as file: # Open html file with read permission
    data = file.read().replace('\n', '') # Remove lines break to have a string instead of a list
    for id in string_ids: # Search for the strings to replace in the html string
        data = data.replace(id, content[string_ids.index(id) + 1]) # replace them by the result of the sql command
    print(data)
    file.close()
