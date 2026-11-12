#Functions are a block of reusable code where logic will be defined in the parent module
#and execution can be performed in any one of the child module.

#.py file extension called-module

#Syntax: def function_name(): -> definition or declaration of function.
             #block of codes
        #function_name() -> calling or invokation of function

#Write a python function to print Hello world
# def message(): #Non Parameterized
#     print("Hello World")

# print("Hi")
# message()

#Type of functions: Parameterized and non parameterized-
# def greeting(name): #Parameter list
#     print(f"Hello dear {name}")
# greeting("sachin")
# greeting("Ashok")

#The value passed through invokation or calling is called as Argument.
#The variable that stores the argument is called as Parameters.
#This together is called as parameterized.

#Type of parameters: All data types

# def student(name,age,place,contact):
#     print(f"{name}-{age}-{place}-{contact}")
# student("Nithesh",30,"cochin",[4578,1234])

#Default Parameters:
# def student(name,age,place,contact,grade="5th grade"):
#     print(f"{name}-{age}-{place}-{contact}-{grade}")
# student("Nithesh",30,"cochin",[4578,1234])
# student("Sachin",30,"Palakkad",[456,789],"6th grade")

#Arbitrary Arguments: (*args)
# def details(*data):
#     print(data)
# details("Nithesh",30,"cochin",[4578,1234]) #It will converts to Tuple

#Keyword Arguments:
# def details(age,name):
#     print(age,name)
# details(name="suresh",age=30) #It will fetch values using key

#Arbitary keyword arguments:(**kwargs) to accpet any number of arguments
# def details(**data):
#     print(data)
# details(name="suresh",age=30)
# details(name="Varun",age=30,place="ernakulam")

#Return statement: Immediately stops the function after calling.
# def addition(a,b):
#     # print(a+b)
#     return a*b #Functions can return values using the return statement

# x=addition(20,30)
# print(x)

#Scope of a Variable: scope means the area of a pgm where a variable can be accessed or used.
#There are two types of scopes: Local adn Global scope.
# 1.Local variable: It is a variable declared inside a function, can be accessed only inside the function

# def show():
#     name="abc"
#     print(name)
# show()
# print(name) - Error observed variable can be accessed only inside the function.

#2.Global Variable: It is declared outside all functions and can be accessed both inside and outside functions
# name="abc"
# print(name)
# def show1():
#     name="suresh" #Local Variable
#     print(name)
# show1()
# print(name)

#Using global keyword we can modify the scope of a locally declared variable
name="abc"
print(name)
def show1():
    global name ,x #Converted Local to global using keyword
    name="suresh" #Local Variable
    print(name)
    x=20
show1()
print(name)
print(x)

