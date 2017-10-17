'''Daria Shifrina, Alessandro Cartegni
SoftDev1 pd 7
HW09 - no treble
2017-10-15
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
#==========================================================
#HELPER FUNCTIONS
#==========================================================
#dictionary from file, returns dictionary

def create_dict_from_file(file):
    dict_file = open(file)
    return csv.DictReader(dict_file)

#############################################    
#finds grade average, return average

def average(student):
    sum = 0
    length = 0
    for grade in student['grades']:
        sum += grade
        length += 1
    return sum/length
#############################################
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
            stu_grades[stu]['average'] = average(stu_grades[stu])
        else:
            stu_grades[stu] = {}
            stu_grades[stu]['average'] = grade
            stu_grades[stu]['grades'] = []
            stu_grades[stu]['stuid'] = stuid
            stu_grades[stu]['grades'].append(grade)
    return stu_grades
#############################################
def update_average(student):
    stu_grades= dict_builder()
    new_average = average(stu_grades[student])
    commandp = "UPDATE peeps_avg SET average = " + str(new_average) + " WHERE id = " + str(stu_grades[student]['stuid'])
    c.execute(commandp)
    stu_grades[student]['average'] = new_average
#############################################
def update_courses(code, mark, classid):
    command2 = "INSERT INTO courses VALUES ('" + code + "', " + str(mark) + ", " + str(classid) + ")"
    c.execute(command2)
#############################################
def print_stu_grades():
    for stu in stu_grades:
        grades = str(stu_grades[stu]['grades'])
        grades = grades.replace("[", "")
        grades = grades.replace("]", "")
        print('Student Name: ' +  stu  + ', ID: ' + str(stu_grades[stu]['stuid'])  + ", Grades: " + grades + ", Grade Average: " + str(stu_grades[stu]['average']))
#==========================================================

#creating database and stuff

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#TESTING EVERYTHING

#creating dicts for courses and peeps
dict1 = create_dict_from_file('courses.csv')
dict2 = create_dict_from_file('peeps.csv')

#creating tables
command_courses = "CREATE TABLE courses(code text, mark integer, id integer)"
  #put SQL statement in this string
c.execute(command_courses)    #run SQL statement
command_peeps = "CREATE TABLE peeps(name text, age integer, id integer)"
c.execute(command_peeps)
command_peeps_avg = "CREATE TABLE peeps_avg(id integer, average numeric)"
c.execute(command_peeps_avg)    #run SQL statement

#putting info in tables
for key in dict1:
    command_dict1 = "INSERT INTO courses VALUES ('" + key['code'] + "'," + key['mark'] + "," +  key['id']  + ")"
    c.execute(command_dict1)
for key in dict2:
    command_dict2 = "INSERT INTO peeps VALUES ('" + key['name'] + "'," + key['age'] + "," +  key['id']  + ")"
    c.execute(command_dict2)

#building dictionary for peeps_avg tables
stu_grades = dict_builder()

print("Before Updating Average")

print_stu_grades()

for poop in stu_grades:
    command2 = "INSERT INTO peeps_avg VALUES ('" + str(stu_grades[poop]['stuid']) + "'," + str(average(stu_grades[poop]))  + ")"
    c.execute(command2)

print("######################################################\nAfter inserting into course: carpentry, 56, 1 and updating average of kurder(who has id 1):")

update_courses("carpentry",56,1)

update_average("kruder")

print_stu_grades()




#==========================================================
db.commit() #save changes
db.close()  #close database'''


