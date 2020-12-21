'''create a SQLITE database or use an existing database and create a table in the database called "Ages"
Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands.
Once the inserts are done, run the following SQL command.
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.'''

CREATE TABLE Ages (
	name VARCHAR(128),
	age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name,age) VALUES ('McCaulley', 31);
INSERT INTO Ages (name, age) VALUES ('Yadgor', 36);
INSERT INTO Ages (name, age) VALUES ('Blaike', 35);
INSERT INTO Ages (name, age) VALUES ('Ireoluwa', 16);
INSERT INTO Ages (name, age) VALUES ('Barath', 16);

SELECT hex(name || age) AS X FROM Ages ORDER BY X LIMIT 1;