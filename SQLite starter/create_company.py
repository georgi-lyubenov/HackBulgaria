import sqlite3

conn = sqlite3.connect("my_company.db")
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS my_company (id INTEGER PRIMARY KEY, name TEXT,
            monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
''')

# Insert a row of data
c.execute("INSERT INTO my_company VALUES (1,'Ivan Ivanov',5000,10000,'Software Developer')")
c.execute("INSERT INTO my_company VALUES (2,'Rado Rado',500,0,'Technical Support Intern')")
c.execute("INSERT INTO my_company VALUES (3,'Ivo Ivo',10000,100000,'CEO')")
c.execute("INSERT INTO my_company VALUES (4,'Petar Petrov',3000,1000,'Marketing Manager')")
c.execute("INSERT INTO my_company VALUES (5,'Maria Georgieva',8000,10000,'COO')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

