import sqlite3

conn = sqlite3.connect("tables.db")
c = conn.cursor()
c.execute('''PRAGMA goreign_keys = ON;''')

c.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, name TEXT,
            rating INTEGER)
''')

c.execute("INSERT INTO movies VALUES (1,'The Hunger Games: Catching Fire',7.9)")
c.execute("INSERT INTO movies VALUES (2,'Wreck It Ralph',7.8)")
c.execute("INSERT INTO movies VALUES (3,'Her',8.3)")


c.execute('''CREATE TABLE IF NOT EXISTS projections (id INTEGER PRIMARY KEY,
            movie_id INTEGER FOREIGN KEY REFERENCES movies(id) ,type TEXT,
            date TEXT, time TEXT)
''')

c.execute("INSERT INTO projections VALUES (1, 1, '3D', '2014-04-01', '19: 10')")
c.execute("INSERT INTO projections VALUES (2, 1, '2D', '2014-04-01', '19: 00')")
c.execute("INSERT INTO projections VALUES (3, 1, '4DX', '2014-04-02', '21: 00')")
c.execute("INSERT INTO projections VALUES (4, 3, '2D', '2014-04-05', '20: 20')")
c.execute("INSERT INTO projections VALUES (5, 2, '3D', '2014-04-02', '22: 00')")
c.execute("INSERT INTO projections VALUES (6,2, '2D', '2014-04-02', '19: 30')")

c.execute('''CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY, username TEXT,
            projection_id INTEGER FOREIGN KEY REFERENCES projections(id), row INTEGER unique, col INTEGER unique)
''')

c.execute("INSERT INTO reservations VALUES (1,'RadoRado',1,2,1)")
c.execute("INSERT INTO reservations VALUES (2,'RadoRado',1,3,5)")
c.execute("INSERT INTO reservations VALUES (3,'RadoRado',1,7,8)")
c.execute("INSERT INTO reservations VALUES (4,'Ivo',3,1,1)")
c.execute("INSERT INTO reservations VALUES (5,'Ivo',3,1,2)")
c.execute("INSERT INTO reservations VALUES (6,'Mysterious',5,2,3)")
c.execute("INSERT INTO reservations VALUES (7,'Mysterious',5,2,4)")


conn.commit()
conn.close()
