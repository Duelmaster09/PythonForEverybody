'''This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and 
populate the tables from the data file.
You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - 
this code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.
Each student gets their own file for the assignment. Download this file and save it as roster_data.json. Move the downloaded file into the same folder as your roster.py program.'''

import sqlite3
import json

conn=sqlite3.connect('AssignmentsDB.sqlite')
cur=conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id,course_id)
    );
''')

inputfile=input('Enter JSON file name: ')
data=open(inputfile).read()
json_data=json.loads(data)

for record in json_data:
    name=record[0]
    course=record[1]
    role=record[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
    cur.execute('SELECT id FROM User WHERE name=?',(name,))
    user_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(course,))
    cur.execute('SELECT id FROM Course WHERE title=?',(course,))
    course_id=cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id,course_id,role) VALUES (?,?,?)',(user_id,course_id,role))

conn.commit()