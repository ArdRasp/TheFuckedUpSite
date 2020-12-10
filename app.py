from flask import Flask, render_template, url_for
from random import randint
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    sqlite_connection = sqlite3.connect("./whoareyou.db")
    cursor = sqlite_connection.cursor()
    cursor.execute('SELECT * FROM data ORDER BY id LIMIT 1 OFFSET ' + str(randint(0, 1000)) + ';')
    line = list(cursor.fetchone())
    class Person:
        first_name = line[1]
        last_name = line[2]
        email = line[3]
        num = line[4]
        country = line[5]
    sqlite_connection.close()
    return render_template("index.html", Person=Person)

if __name__ == "__main__":
    app.run(debug=True)
