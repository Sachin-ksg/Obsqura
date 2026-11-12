#keywords : if ,elif , else

"""#input an age from the user and check whether he is minor or not.

age=int(input("Enter your age:"))
if age >= 18:
    print("Your eligible")
else:
    print("your not eligible")"""

#input an age and nationality from the user and check whether he is eligible for voting or not.

"""age=int(input("Enter your age:"))
nationality=input("Enter your nationality:").lower()

if age>=18 and nationality=="indian":
    print("Your eligible")
else:
    print("your not eligible") """

#Input a number from user and check whether it is even or odd.

"""num1=int(input("Enter a number:"))
if num1%2==0:
    print("Number is even")
else:
    print("Number is odd")"""


#Input a number and check it is positive, negative or Zero

"""a=int(input("Enter a number:"))
if a>0:
    print(f"{a} is positive")
elif a==0:
    print(f"{a} is Zero")
else:
    print(f"{a} is negative") """

#Input 3 numbers and check which one is great

num1,num2,num3=100,20,300

if num1>num2 and num1>num3:
    print(f"{num1} is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")