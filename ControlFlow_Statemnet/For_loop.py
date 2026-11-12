#Write a python pgm to print "Hello World" 10 times.
#syntax: for item in iterable
#Iterables : String, List, Tuple, Set,Dictionary, range of numbers
# Iterate : means to go through each item in a sequence one by one.
# Iteration is one complete repetition of a process in a loop.

"""for item in range(10): #[0,1,2,...9]
    print(item,"-Hello World")
print("Hi")"""

#Write python pgm to iterate first 10 natural numbers (1,2,...10)
#Syntax of range: (starting index,ending index+1,step)
"""for i in range(1,11):
    print(i) """

#Write python pgm to iterate numbers 15 to 35
"""for i in range(15,36):
    print(i)"""
#Write python pgm to iterate first 10 natural numbers and print all even numbers:
#method1:
#for i in range(2,11,2):
#   print(i)
#method2:
"""for i in range(1,11):
    if i%2==0:
        print(i)"""

#Write python pgm to iterate first 10 natural numbers and get even and odd numbers separate list:
"""even=[]
odd=[]
for i in range(1,11):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)"""

#Write python pgm to iterate first 10 natural numbers and get the square of all numbers in separate list

"""square=[]
for i in range(1,11):
    square.append(i**2)
print(square)"""

#Write python pgm to iterate first 10 natural numbers and get the sum of squares.

"""total=0
for i in range(1,11):
    total+=i**2
print(total)"""

#Sum of first 20 natural numbers:
"""total=0
for i in range(1,21):
    total+=i
print(total)"""

#Get the product first 10 natural numbers:
#Get the sum of cubes of first 5 natural numbers.
#Get the sum of cubes of first 10 even numbers.

# lis1=[10,20,30,40]
# for i in lis1:
#     print(i)
# tup=(20,30,40,"hello")
# for item in tup:
#     print(item, end=" ")

# s="hello"
# for i in s:
#     print(i)
# s="hello-gud mor-ning"
# print(s.split("-"))
#
# s="python training"
# for i in s.split():
#     print(i)

dict1={"name":"sachin","age":30}
for key,value in dict1.items():
    print(key,value)

