# list6=[10,20,30,40]
# name="apple"
# #list6.insert(2,"apple")
# list6.insert(2,name)
# print(list6)
#expected output: list7=[10,20,"apple",30,40]

#write a function to count vowels in a string

# def vow(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in s:
#         if i in vowels:
#             count+=1
#     print(count)
# vow("python programming")


#create a function t check whether a test case has passed or failed

# output_txt="12 tests passed"
# output_txt1="10 Passed and 2 Failed"
# def check_test_status(status):
#     if "Failed" in status:
#         print("Test Failed, Please try Again")
#     else:
#         print("Test Passed")
# check_test_status(output_txt)
# check_test_status(output_txt1)

#create a function to check whether a username is valid [length more than 5]
username=input("Enter the username:")
def status(username):
    if len(username)>5:
        return True
    else:
        return False
print(status(username))


#create a function to validate an email address
#can include characters, digits,.,com/in,gmail,@ and always starts with character.

# email=input("Enter a mail id:")
# def validate(email):
#     #firstchar=email[0]
#     #print(type(firstchar))
#     if "@" in email and "." in email and "gmail" in email and ".com" in email or ".in" in email:
#         print("Email is valid")
#     else:
#         print("Email is not valid")
# validate(email)

# email=input("Enter a mail id:")
# def validate(email):
#     firstchar=email[0]
#     if (not firstchar.isdigit()) and "." in email and "@" in email and "gmail" in email and ".com" in email or ".in" in email:
#         print("Email is valid")
#     else:
#         print("Email is not valid")
# validate(email)
#
# #create a function to convert a browser name into lowercase
#
# browser=input("Enter a browser name:")
# def lower(browser):
#     print(browser.lower())
#
# lower(browser)

#in case of strict check always use "=="
#in case of return statement , check all conditions are fullfilled in prior
#Default arguments, passing arguments
#Always use return statement when we want to store the output.
#In print() execution continuos after print(), iN return execution will stop after return().
