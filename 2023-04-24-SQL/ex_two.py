import sqlite3

conn = sqlite3.connect("my_new_db.db")
conn2 = sqlite3.connect("my_new_db_2.db")
c = conn.cursor()
c2 = conn2.cursor()

with conn:
    c.execute("DROP TABLE IF EXISTS paskaitos")

with conn2:
    c2.execute("DROP TABLE IF EXISTS paskaitos")

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    paskaitos (
    pavadinimas text,
    destytojas text,
    trukme integer
    )""")
with conn2:
    c2.execute("""CREATE TABLE IF NOT EXISTS
    paskaitos (rowid INTEGER PRIMARY KEY) """)

with conn:
    c.execute("INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80), ('Java', 'Tomas', 80)")

with conn:
    c.execute("""SELECT * FROM paskaitos where trukme > 50""")
    print(f"Lectures which have duration longer than 50 {c.fetchall()}")
   
with conn:
    c.execute("""UPDATE paskaitos SET pavadinimas = 'Python programavimas' where pavadinimas = 'Python'""")

with conn:
    c.execute("""DELETE FROM paskaitos where destytojas = 'Tomas'""")

with conn:
    c.execute("SELECT * from paskaitos")
    # for lecture in c.fetchall():
    #     print(lecture)
    print(f"Entire table {c.fetchall()}")

with conn:
    c.execute("SELECT * FROM paskaitos")
    desc = c.description
    column_names = [col[0] for col in desc]
    for name in column_names:
        with conn2:
            c2.execute(f"ALTER TABLE paskaitos ADD COLUMN {name} varchar(32)")
    c2.executemany("INSERT INTO paskaitos(pavadinimas, destytojas, trukme) VALUES (?,?,?)", c.fetchall())

with conn2:
    c2.execute("SELECT * FROM paskaitos")
    print(c2.fetchall())

with conn:
    c.execute("SELECT * FROM paskaitos")
    desc = c.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row)) for row in c.fetchall()]

    print(data)

