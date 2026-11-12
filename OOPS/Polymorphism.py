"""Polymorphism means one name with many forms, it allows same method name(function)
or operator to behave differently depending on the object"""

#The built in polymorphic opertaor in python is "+", (for numbers ut will perform addition, for string it will perform concatenation)


class Parent:
    def skill(self):
        print("Teaching Skill")
class child(Parent):
    def skill(self):
        super().skill()
        print("Singing")
class child2(Parent):
    def skill(self):
        print("HR")
        super().skill()

obj=child()
obj.skill()
obj2=child2()
obj2.skill()

"""In Python the type of polymorphism it support is method overriding,
It is the scenario in which same method is defined (with a different performance)

#Overloading:
same method is using more than once in a class, there is no inheritance in this case,Not supported in Python
only final method will considered"""

#Method overloading:

class Parent:
    def addition(self):
        print("Adddition of numbers")
    def addition(self,a,b):
        print(a+b)
obj=Parent()
obj.addition(1,2)
obj.addition(5,6)

