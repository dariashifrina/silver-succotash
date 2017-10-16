'''Daria Shifrina
SoftDev1 pd 7
HW09 - no treble
2017-10-15
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

dict_file1 = open('courses.csv')
dict_file2 = open('peeps.csv')
dict1 = csv.DictReader(dict_file1)
dict2 = csv.DictReader(dict_file2)
f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


command = "CREATE TABLE courses(code text, mark integer, id integer)"
  #put SQL statement in this string
c.execute(command)    #run SQL statement
command = "CREATE TABLE peeps(name text, age integer, id integer)"
c.execute(command)
for key in dict1:
    command1 = "INSERT INTO courses VALUES ('" + key['code'] + "'," + key['mark'] + "," +  key['id']  + ")"
    c.execute(command1)

for key in dict2:
    command2 = "INSERT INTO peeps VALUES ('" + key['name'] + "'," + key['age'] + "," +  key['id']  + ")"
    c.execute(command2)

q = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id"
foo = c.execute(q)
for bar in foo:
    print bar[2]

command3 = "CREATE TABLE averages(name text, id integer, marks text, average numeric)"
c.execute(command3)

#==========================================================
db.commit() #save changes
db.close()  #close database'''
