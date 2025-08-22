import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Darby', 24532, 'darby@email.com')")

curser = db.cursor()
curser.execute("SELECT * FROM contacts")
for row in curser:
    print(row)

curser.close()
db.close()
