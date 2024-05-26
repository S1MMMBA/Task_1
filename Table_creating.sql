 CREATE TABLE Rooms
 (
	 id INTEGER PRIMARY KEY,
	 name VARCHAR(15)
 );
 CREATE TABLE Students
 (
	 birthday DATE,
	 id INTEGER PRIMARY KEY,
	 name VARCHAR(30),
	 room INTEGER,
	 sex VARCHAR(1),
	 FOREIGN KEY (id) REFERENCES Students(id)
 )