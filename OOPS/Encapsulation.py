"""It is the process of combining data (Variable) and methods (functions) into a single unit
called a Class and while controlling access to the data
Python has 3 common access levels called as Access modifiers
1.public: (name="Sachin") can be accessed normally
2.Protected:(_name="Sachin") indented for internal or subclass uses
3.Private: (__name="Sachin") can be accessed only using base class objects"""

"""example for Protected variable- Password
example for Private method - Balance Enquiry using ATM card"""

class Employee:
    def __init__(self,name,salary,password):
        self.name=name #public variable
        self._salary=salary #protected variable
        self.__password=password #Private variable
    def display_name(self):
        print(f"Employee name is {self.name}")
    def _display_salary(self):
        print(f"Employee salary {self._salary}")
    def __display_password(self):
        print(f"Employee Password {self.__password}")

    def show_details(self):
        self.__display_password()

obj=Employee("Sachin",40000,"ABC")

#Accessing public variable and method:
print(obj.name)
obj.display_name()
#Accessing Protected Variable and method.

print(obj._salary)
obj._display_salary()

#Accessing Private variable and method
# print(obj.__password)
# obj.__display_password() #Cannot access private variable and method directly
obj.show_details()

#Getter and setter methods:
""""getter method used to retrieve the value of a private variable
setter method is used to modify the value of a private variable usually with validation"""



