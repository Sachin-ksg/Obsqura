"""Inheritance: it is the concept in which one class acquires the properties of another class
The first class is called as-Parent , Base, Super Class is None:
The Second class called as- Child class, sub class , derived class, inherited class"""
"""A child class can reuse the code of a parent class without writing it again"""

class Parent:
    networth="10Crore"
    def skill(self):
        print("Teaching skill")

class Child(Parent):
    def job(self,jobtitle):
        print(f"The Job title is {jobtitle}")

c=Child()
print(c.networth)
c.skill()
c.job("HR")

"""Type of Inheritance: Single Inheritance: one parent and one child
Multiple Inheritance: Different parent class and one child class"""

"""Multi Level Inheritance: A child class becomes a parent class for another class
Hierarechical Inheritance: Single parent and different child class
Hybrid Inheritance: It can be a combination of two or more inheritance"""


#Multiple Inheritance:
class A:
    pass
class B:
    pass
class C(A,B):
    pass

obj=C()

#Multilevel Inheritance:
class A:
    pass
class B (A):
    pass
class C(B):
    pass

obj1=C()

#Hierarechical :
class Parent:
    def display(self):
        print("Parent Method")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

obj2=Child1()
obj3=Child2()
obj2.display()
obj3.display()