'''This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) 
using a database with the following schema to maintain the counts.
When you have run the program on mbox.txt upload the resulting database file above for grading.'''

import sqlite3

conn=sqlite3.connect('AssignmentsDB.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
    CREATE TABLE Counts (
        org TEXT,
        count INTEGER
    ) 
''')

inputfile=input('Enter File Name: ')
fh=open(inputfile)

for line in fh:
    line=line.strip()
    if line.startswith('From: '):
        org=line.split()[1].split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org=?',(org,))
        row=cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org,count) Values (?,1)',(org,))
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(org,))

conn.commit()