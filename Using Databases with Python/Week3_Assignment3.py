'''This application will read an iTunes export file in XML and produce a properly normalized database with this structure.'''

import xml.etree.ElementTree as et
import sqlite3

conn=sqlite3.connect('AssignmentsDB.sqlite')
cur=conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
        name TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
        name TEXT UNIQUE
    );

    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
        artist_id INTEGER,
        title TEXT UNIQUE
    );

    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER,
        rating INTEGER,
        count INTEGER
    );
''')

fname=input('Enter XML file name: ')
fh=open(fname)

def lookup(record,key):
    found=False
    for element in record:
        if found:
            return element.text
        if element.tag=="key" and element.text==key:
            found=True
    return None

data=et.parse(fh)
all_records=data.findall('dict/dict/dict')
for record in all_records:
    if not lookup(record,'Track ID'):
        continue
    artist=lookup(record,'Artist')
    genre=lookup(record,'Genre')
    album=lookup(record,'Album')
    track=lookup(record,'Name')
    length=lookup(record,'Total Time')
    rating=lookup(record,'Rating')
    count=lookup(record,'Play Count')

    if artist is None or album is None or track is None or genre is None:
        continue

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name=?',(artist,))
    artist_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES(?)',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name=?',(genre,))
    genre_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (artist_id,title) VALUES (?,?)',(artist_id,album))
    cur.execute('SELECT id FROM Album WHERE title=?',(album,))
    album_id=cur.fetchone()[0]

    cur.execute('''
        INSERT OR REPLACE INTO Track (title,album_id,genre_id,len,rating,count) 
        VALUES (?,?,?,?,?,?)
    ''',(track,album_id,genre_id,length,rating,count))

conn.commit()