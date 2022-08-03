from distutils.command.build_scripts import first_line_re
import email
from getpass import getuser
from matplotlib.pyplot import get
import names as nm
import pandas as pd
import random
from datetime import date, timedelta

def getfirstname(gen):
    return nm.get_first_name(gender=gen)

def getlasstname():
    return nm.get_last_name()

def getfullname(first,last):
    return first+" "+last

def getusername(fullname,suffiks):
    return fullname.replace(" ","").lower()+str(random.randint(10**(suffiks-1),10**suffiks))

def getemail(username,mail):
    return username+mail

def getgender(gen):
    if gen == True:
        return "Male"
    else:
        return "Female"

def getbirthday(rangeyear1,rangeyear2):
    return str(date(random.randint(rangeyear1,rangeyear2),random.randint(1,12),random.randint(1,28)))

def getalldata(gen,suffiks,mail,rangeyear1,rangeyear2):
    firstname = getfirstname(gen)
    lastname = getlasstname()
    fullname = getfullname(firstname,lastname)
    username = getusername(fullname,suffiks)
    email = getemail(username,mail)
    gender = getgender(gen)
    birthday = getbirthday(rangeyear1,rangeyear2)

    return email,firstname,lastname,fullname,username,gender,birthday

#main

numberemail = int(input('How many email will you create ? '))
gen = random.choice([True,False])
suffiks = int(input('How many suffiks you will add in username ?  '))
mail = str(input('What domain email will use ? '))
rangeyear1 = int(input('range bitrhday year 1 ? '))
rangeyear2 = int(input('range bitrhday year 2 ? '))

alldata = []

for i in range(numberemail):
    email,firstname,lastname,fullname,username,gender,birthday = getalldata(gen,suffiks,mail,rangeyear1,rangeyear2)
    dataperson = [email,firstname,lastname,fullname,username,gender,birthday]
    alldata.append(dataperson)

df = pd.DataFrame(alldata,columns=("email","firstname","lastname","fullname","username","gender","birthday"))
print(df)
