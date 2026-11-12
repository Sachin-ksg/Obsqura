#Error: A pbm in apgm that prevents it from working as intended.
#Reasons: in correct syntax, incorrect pgm logic, invalid operations

#eg:
# if 10>5
#     print("Hello") example for syntax error

# print(name) #name error

# list1=[10,20,30]
# print(list1[5]) #list index out of range

# num=int("hello") #ValueError: invalid literal for int() with base 10: 'hello'

# print(10/0) ZeroDivisionError: division by zero

# dict1={"name":"sachin","age":30}
# print(dict1["location"]) #KeyError: 'location'

#Exception: Its an error that occurs during pgm execution and interrupts the normal flow of the pgm

#Try and Except:
# try:
#     #Code that may cause an exception
# except:
    # code to handle the exception
#else:
#executes when no exception occurs
#finally:
#executes irrespective of exception

# try:
#    n=int(input("Enter a number:"))
#    result=100/n
#    print(result)
# except ValueError:
#     print("Please enter a valid integer")
# except ZeroDivisionError:
#     print("Please enter a non zero value")
#
# print("Hello")

# try:
#    n=int(input("Enter a number:"))
#    result=100/n
# except ValueError:
#     print("Please enter a valid integer")
# except ZeroDivisionError:
#     print("Please enter a non zero value")
# else:
#     print(result)
#     print("No exception occured")
# finally:
#     print("Pgm execution completed")

#Raising exceptions using raise keyword - if want to generates an intentional exception
#when particular condition occurs.

# age=17
# if age<18:
#     raise ValueError("Age must be 18 or above")
# print("Eligible")

def withdraw(balance,amount):
    if amount>balance:
        raise ValueError("Insufficient Balance")
    else:
        return balance-amount
x=withdraw(100,50)
print(x)
y=withdraw(100,250)
print(y)

#Exception handling in Playwright:
#1.Elements not found
#2.Locator takes too long to take actionable
#3.Browser gets closed unexpectedly