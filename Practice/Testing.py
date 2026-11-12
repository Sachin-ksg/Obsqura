#Write a python pgm to check whether the number is prime or not
#prime numbers-2,3,5,7,11,13,17..(those numbers which are divisible by one and same numbers only)
#consider 7 (Divide using 2,3,4,5,6) if remainder is zero any case the number is not prime.
#consider 9 (Divide 2 to 8)

# n=int(input("Enter a number:"))
# if n<2:
#     print("Not in Prime number range")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print(f"{n} is not prime")
#             break
#     else:
#         print(f"{n} Number is Prime")

#Find the prime numbers in range 10 to 30.
# prime=[]
# for num in range(10,31):
#     if num<2:
#         print("number is not in prime number range")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
# print(prime)


#Find the count of prime numbers in range 10 to 30.
# prime=[]
# count=0
# for num in range(10,31):
#     if num<2:
#         print("number is not in prime number range")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
#             count+=1
# print(prime)
# print(len(prime))
# print(count)

#Input a number from user and reverse it(input: 541 output:145)
# n=541
# reverse=0
# while (n>0):
#     digit=n%10
#     reverse=reverse*10+digit
#     n//=10
# print(reverse)
#in first iteration n=541 digit=1, reverse=0*10+1=1 ,n=54
#in second iteration n=54, digit=4, reverse=1*10+4=14, n=5
#in third iteration n=5,digit=5, reverse=14*10+5=145, n=0
#in 4th iteration condition False and while loop breaks.

#input a number from user and find the sum of digit of the number.
#input:541 output: 10 (5+4+1)

# n=541
# org=n
# s=0
# while(n>0):
#     s+=n%10
#     n//=10
# print(f"The sum of digits of {org} is: {s}")

#Input a string from user and remove all the duplicate characters
#input: "programming" output: progamin

# s="programming"
# result=""
# for i in s:
#     if i not in result:
#         result+=i
# print(result)

#Input two numbers from user and swap it
#input: a,b=10,20
#output: a,b=20,10
# a=10
# b=20
# a,b=b,a
# print(a,b)

#find the largest number in a list without using index position.
#input list x=[100,10,-1,1200,11,3]
#output 1200
largest=0
x=[100,10,-1,1200,11,3]
for i in x:
    if i>largest:
        largest=i
print(largest)

#The Fibonacci series starts with 0 and 1.
# Each subsequent number is the sum of the previous two numbers.

n = int(input("How many terms? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

