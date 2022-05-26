import psycopg2

connection = psycopg2.connect('dbname=proxy1 user=postgres password=root')

cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE account (
                   id INTEGER PRIMARY KEY,
                   accountName VARCHAR(100),
                   isActive BOOLEAN NOT NULL DEFAULT True
               );
               """)

cursor.execute("INSERT INTO account (id, accountName, isActive) VALUES(1, 'Yahaya Ahmad', True)") 

connection.commit()

connection.close()
cursor.close() 

