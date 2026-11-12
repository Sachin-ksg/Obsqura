#First 10 natural numbers:

# for i in range(1,11):
#     print(i)

# i=1
# while(i<=10):
#     print(i)
#     i+=1

#Iterate numbers 20 to 40:

# i=20
# while (i<=40):
#     print(i)
#     i+=1

#Iterate first 10 natural numbers in reverse order:
# i=10
# while(i>0):
#     print(i)
#     i-=1

#A for loop is generally used when we want to iterate over a sequence or repeat to a known number of times.
  #eg: iterate 1 to 5, iterate  1 to 10.
#A while loop is used when we want to repeat a block of code as long as the condition is True.
 #eg: To login with valid credentials, ATM cah withdrawal using PIN

#Write a python pgm to find the factorial of a number:
# eg: for the number 5 factorial= 1*2*3*4*5 =120

# num=int(input("Enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(f"The factorial of {num} is :{fact}")

#Write a python pgm that repeatedly ask the user to enter a user name and password  until both credentials are correct

username="admin"
pwd="admin123"

user1=""
pwd1=""
while(user1!=username or pwd1!=pwd):
    user1 = input("Enter username:")
    pwd1 = input("Enter pwd:")
    if user1 != username or pwd1!=pwd:
        print("Invalid credentials try again")
print("Login Successful")

#ATM Pin Verification- provide a valid pin number ,get a pin from user and check validity.
