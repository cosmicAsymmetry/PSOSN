import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",
                     port = 3306,# your username
                     passwd="sidhantB27",  		  # your password
                     db="psosm")          # name of the data base

# you must create a Cursor object. It will let you execute all the queries you need

cursor = db.cursor()


#Let us query the data base we created yesterdday

query = "SELECT * FROM tutorial"
cursor.execute(query)
rows = cursor.fetchall()

print rows

#query = "INSERT ignore into tutorial (id, name) values (8,'Naman')"

#cursor.execute(query)
#db.commit()

name = "Divyansh"
age = 22
affiliation = "NSIT"
interest = "Programming" #Difficult to store a list in a single column. Relational databases are designed specifically to store one value per row/column combination.


#Let's create a new table where we will add the detailed presenter info

"""
query = "Create table detailed_participants ( name varchar(20) NOT NULL, age INT NOT NULL, affiliation varchar(10), interest varchar(20))"
cursor.execute(query)
db.commit()
cursor.close()

"""

query = "insert ignore into detailed_participants (name,age,affiliation,interest) values (%s,%s,%s,%s);"

cursor.execute(query, (name, age, affiliation, interest))
db.commit()

exit()

"""
query = "update detailed_participants set name = 'Divyansh Agarwal' where name = 'Divyansh'"
cursor.execute(query)
db.commit()

db.close()  #Closes the connection
"""
