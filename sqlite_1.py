import sqlite3

# 1 konekcija na bazu podataka (ako baza ne postoji, biće kreirana)
conn = sqlite3.connect('chinook.db')

# 2 kreiranje kursora
c = cursor = conn.cursor()

# 3 izvršavanje SQL upita EXECUTE
# -- SELECT * FROM albums
# -- SELECT * FROM albums WHERE artistid = 10
# -- SELECT * FROM albums WHERE artistid BETWEEN 10 AND 15

# SELECT * FROM albums WHERE title like '%Bi%'

# -- SELECT * FROM albums WHERE artistid BETWEEN 10 AND 15
c.execute('''SELECT * FROM albums WHERE artistid BETWEEN ? AND ?''', (10, 15))

#3.1. Dohvat iz baze podataka - fetchall, fetchone, fetchmany
# results = c.fetchall()  # dohvat svih rezultata

#3.2 prikaz svih rezultata
results = c.fetchall()    
    
print(results)
# 4 zatvaranje konekcije
conn.close()
# results = c.fetchone()  # dohvat jednog rezultata
# results = c.fetchmany(3)  # dohvat prvih 3 rezultata
