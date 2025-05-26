import csv
import sqlite3


conn = sqlite3.connect("crassistant.db")

cursor = conn.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)
#to insert values
#query = "INSERT INTO sys_command VALUES (NULL, 'Chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')"
#cursor.execute(query)
#cursor.execute("UPDATE sys_command SET path = ? WHERE id = ?", ('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 1))
#conn.commit()
#conn.close()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#to insert values
#query = "INSERT INTO web_command VALUES (NULL, 'Instagram','https://instagram.com')"
#cursor.execute(query)
#conn.commit()
#conn.close()

#updating url  not working
'''
query = "UPDATE web_command SET url = 'https://canva.com' WHERE id = 1"
cursor.execute(query)
conn.commit()
conn.close()

#testing module
query = "OneNote"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
results = cursor.fetchall()
print(results[0][0])
'''
'''
query = "Drop TABLE IF EXISTS sys_command"
cursor.execute(query)
conn.commit()
conn.close()
'''

#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


#0-based index
#example : importing 1st and 3rd colmns
#desired_columns_indices = [0, 1]

#read data from csv and insert into SQLite table for desired columns
#with open('contacts.csv','r', encoding='utf-8') as csvfile:
#   csvreader = csv.reader(csvfile)
#   for row in csvreader:
#       selected_data = [row[i] for i in desired_columns_indices]
#       cursor.execute('''INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null,?,?);''', tuple(selected_data))
#commit changes and close connection
#conn.commit()
#conn.close()


#to insert contacts manually
#'''
#query = "INSERT INTO contacts VALUES (NULL,'Ador', '8801905851443', 'NULL')"
#cursor.execute(query)
#conn.commit()

#'''


#query = 'atika'
#query = query.strip().lower()

#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%'+ query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])