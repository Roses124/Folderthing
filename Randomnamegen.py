#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
Names = ["Stacy ", "Joseph ", "Allison ", "James ", "Josephine ", "Eric ", "Erica ", "Jack "]

#Generates a random integer.
aRandomIndex = randint(0, len(Names)-1)
print(Names[aRandomIndex])
