#Assignment Py
#Author: Eliza Nip
#Date: 02-25-2019

import random
import sys
def randChar():
    return random.choice('abcdefghijklmnopqrstuvwxyz')

#Open randome file 1 and write it.Creat it if not existed. Print out file content aka random lowercase alphabet .
file1 = open("ran1","w")
for x in range(10):
    file1.write(randChar())
file1.write("\n")
file1 = open('ran1','r')
fileLine1 = file1.read()
sys.stdout.write(fileLine1)

#Open randome file 2 and write it.Creat it if not existed. Print out file content aka random lowercase alphabet .
file2= open("ran2","w")
for x in range(10):
    file2.write(randChar())
file2.write("\n")
file2 = open('ran2','r')
fileLine2 = file2.read()
sys.stdout.write(fileLine2)

#Open randome file 3 and write it.Creat it if not existed. Print out file content aka random lowercase alphabet .
file3 = open("ran3","w")
for x in range(10):
    file3.write(randChar())
file3.write("\n")
file3 = open('ran3','r')
fileLine3 = file3.read()
sys.stdout.write(fileLine3)

a =random.randint(1,43)
print(a)
b =random.randint(1,43)
print(b)
print(a*b)

 

