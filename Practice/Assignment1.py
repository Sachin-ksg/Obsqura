#Input a number and check whether it is divisible by 5 or not:

"""a=int(input("Enter a number:"))
if a%5==0:
    print("Number is divisible by 5")
else:
    print("Not divisible by 5") """

#Check a number is +ve or not.

"""b=int(input("Enter a number:"))
if b>=0:
    print("Number is Positive")
else:
    print("Number is Negative")"""

#check a number is 0 or not.

"""c=int(input("Enter a number:"))
if c==0:
    print("Number is zero")
else:
    print("number is not zero")"""

#Input the marks and set the pass mark , then checks pass or fail

"""passmark=75
mark=int(input("Enter Your marks:"))
if mark>=passmark:
    print("PASS")
else:
    print("FAIL")"""

#Enter age set entry fee and check eligibility for discount for senior citizen.
enfee=100
age=int(input("Enter your age:"))
if age>50:
    discount= enfee-enfee/10
    print(f"Eligible for discount and entry fee: {discount}")
else:
    print("Not eligible for discount")





