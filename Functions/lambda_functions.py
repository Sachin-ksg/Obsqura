#It is a small anonymous function written mostly as a single expression using lambda keyword
#unlike a normal function created using def keyword, lambda function doesnot a require a function name
#and explicit return statement.
#Syntax:
#lambda parameters:expression
#expression operation is performed and automatically return as a result.

#Write a function for addition for two numbers:
# def addition(a,b):
#     return a+b
# x=addition(3,4)
# print(x)
#Using lambda function:
# add=lambda a,b:a+b
# print(add(3,4))

#Write a lambda function to find the square of a number:
# square=lambda a:a**2
# print(square(20))

#Checks whether a number is even or odd:
# result=lambda a:"even" if a%2==0 else "odd"
# print(result(9))

#Non parameterixed lambda function:
greet=lambda: "Gud mng"
print(greet())

#String based questions:#1.check whether the given character is a vowel or not (input: x="A")
#2.check whether the given character is a consonant or vowel:
#3.Count the number of vowels in a user input (x="python")
#4.Count the number of vowels in a user input (x="python is easy to learn")

#Loop Based questions:
#1.Get the count of multiples of 5 from the below list (input: x=[1,5,10,15,8,4])
#2.Identify the most repeated element in the given list. List=[5,10,5,10,5,3,2]
#3.Count the number of strings from the below list : List=[5,10,"A","Python","Hello",3.5,False]
