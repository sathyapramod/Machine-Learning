#Declaring variables in python
#Unlike other programming languages, Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.

x = 10
y = "Krishna"

print(x)
print(y)

#Variables do not need to be declared with any particular type and can even change type after they have been set.

x = 4
x = "Vivek" #now x value is Vivek
print(x)

#To combine both text and a variable, Python uses the + character

x = "Python"
print("Welcome to " + x)

#You can also use the + character to add a variable to another variable

x = "Sri"
y = "Krishna"
z = x + y
print(z)

a = 20
b = 40
print(a + b)

#Note: Diffrent data type can't be added like str + int can't be added it will give you error

