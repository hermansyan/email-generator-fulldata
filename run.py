from distutils.command.build_scripts import first_line_re
import names as nm
import pandas as pd
import random

def getfirstname(gen):
    return nm.get_first_name(gender=gen)

def getlasstname(gen):
    return nm.get_last_name(gender=gen)

def getfullname(first,last):
    return first+" "+last

def getusername(fullname,suffiks):
    return fullname.replace(" ","").lower()+str(random.randint(10**suffiks,10**(suffiks+1)))

def getemail(username,mail):
    return username+mail
