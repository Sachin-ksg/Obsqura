"""Constructor is a special method thats get automatically called or invoked when an object is created
Purpose: Initialize objects attributes, Assign Initial value to variable, perform initial setup
"""
# class Parent:
#
#     def __init__(self,name,age):
#         print("Constructor Created")
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Parent Method")
#         print(self.name,self.age)
#
# obj=Parent("Sachin",25)
# obj.display()
# obj2=Parent("Arun",30)
# obj2.display()

"""Destructor:It is a special method python may called when an object is about to be destroyed
Purpose: Perform clean up operations, close files or connections"""

class Parent():
    x=10
    def __init__(self):
        print("Constructor Created")

    def __del__(self):
        print("Destructor Created")

obj=Parent()
del obj
print(obj.x)





