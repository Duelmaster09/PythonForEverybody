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