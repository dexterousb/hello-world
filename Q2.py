#WAP that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#user input name and age
username = input("Enter username:")

#taking age in int(str to int)
age = int(input("Enter age:"))

#covrt int to str to concantenate
x =  str(100-age)
print("You will turn 100 years old after: " + x + " more years :)")
