# import sqlite3

# conn = sqlite3.connect("my_db.db")
# c = conn.cursor()

# with conn:
#     c.execute("""CREATE TABLE IF NOT EXISTS
#     darbuotojai (
#     vardas text,
#     pavarde text,
#     atlyginimas integer
#     )""")

# import sqlite3

# conn = sqlite3.connect("my_db.db")
# c = conn.cursor()

# with conn:
#     c.execute("INSERT INTO darbuotojai VALUES ('Domantas', 'Rutkauskas', 1500)")

#     c.execute("INSERT INTO darbuotojai VALUES ('Rimas', 'Radzevičius', 1000)")

#     c.execute("INSERT INTO darbuotojai (vardas, atlyginimas) VALUES ('Rimas', 1000)")

#import sqlite3

# conn = sqlite3.connect("my_db.db")
# c = conn.cursor()

# with conn:
#     c.execute("SELECT * From darbuotojai WHERE vardas like 'a%'")
#     print(c.fetchall())

#import itertools
# import sqlite3

# conn = sqlite3.connect("my_db.db")
# qu = ("SELECT * From darbuotojai")
# c = conn.cursor()
# c.execute(qu)

# desc = c.description
# column_names = [col[0] for col in desc]
# data = [dict(zip(column_names, row)) for row in c.fetchall()]

# print(data)


import sqlite3

conn = sqlite3.connect("my_db.db")
c = conn.cursor()

with conn:
    c.execute("UPDATE darbuotojai SET atlyginimas=3000 WHERE pavarde='Radzevičius'")

    with conn:
        c.execute("SELECT * From darbuotojai")
        print(c.fetchall())

        