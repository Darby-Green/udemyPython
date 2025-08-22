import sqlite3

db = sqlite3.connect("contacts.sqlite")

newEmail = "newemail@update.com"
phone = input("Please enter your phone number: ")

# updateSQL = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.phone = 24532"
updateSQL = "UPDATE contacts SET email = ? WHERE phone = ?"
print(updateSQL)

updateCursor = db.cursor()
updateCursor.execute(updateSQL, (newEmail, phone))
print("{} rows updated". format(updateCursor.rowcount))
for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()