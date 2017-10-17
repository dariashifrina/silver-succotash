'''Daria Shifrina, Alessandro Cartegni
SoftDev1 pd 7
HW09 - no treble
2017-10-15
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
def create_dict_from_file(file):
    dict_file = open(file)
    dict1 = csv.DicReader(dict_file)
    
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

#student's grades
#q = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id"
#loo = c.execute(q)

###############################################################
#dict builder
def dict_builder():
    q = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id"
    foo = c.execute(q)
    stu_grades = {}
    for bar in foo:
        stu = bar[0]
        stuid = bar[1]
        grade = bar[2]
        if stu in stu_grades:
            stu_grades[stu]['grades'].append(grade)
        else:
            stu_grades[stu] = {}
            stu_grades[stu]['grades'] = []
            stu_grades[stu]['stuid'] = stuid
            stu_grades[stu]['grades'].append(grade)
    return stu_grades
###############################################################

#print dict

stu_grades = dict_builder()

for stu in stu_grades:
    print stu, stu_grades[stu]['stuid'], stu_grades[stu]['grades']

###############################################################

#finds grade average

def average(student):
    sum = 0
    length = 0
    for grade in student['grades']:
        sum += grade
        length += 1
    return sum/length

###############################################################

#testing average
#for stu in stu_grades:
   # print stu, average(stu_grades[stu])

#for stu in stu_grades:
   # grades = str(stu_grades[stu]['grades'])
   # grades = grades.replace("[", "")
   # grades = grades.replace("]", "")
   # print('Student Name: ' +  stu  + ', ID: ' + str(stu_grades[stu]['stuid'])  + ", Grades: " + grades + ", Grade Average: " + str(average(stu_grades[stu])) )

commando = "CREATE TABLE peeps_avg(id integer, average numeric)"
  #put SQL statement in this string
c.execute(commando)    #run SQL statemen

for poop in stu_grades:
    command2 = "INSERT INTO peeps_avg VALUES ('" + str(stu_grades[poop]['stuid']) + "'," + str(average(stu_grades[poop]))  + ")"
    c.execute(command2)
    #print('id: ' + str(stu_grades[poop]['stuid']) + " average; " + str(average(stu_grades[poop])))

def update_average(student):
    stu_grades= dict_builder()
    commandp = "UPDATE peeps_avg SET average = " + average(student) + "WHERE id = " + student['id'] + ")"
    c.execute(commandp)
    
    


#==========================================================
db.commit() #save changes
db.close()  #close database'''


