#Mutable datatypes: List, Set, Dictionary
#Immutable data types: Integer, float, boolean,String, Tuple

#Keywords:They are reserved meaningful words in Python, cannont be provided as variable name
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Difference between Keyword,identifier and variable:
  #Keyword: Reserved meaningful words
  #Variable: Variable declaration can be perform to store or assign values.
  #Variable declaration example:
#Identifiers: Names given to variables, functions,classes,

x=10
X=20
abcABC=30
abc_=14
_abc=16
a_b_c=20
_=50
abc123=35
a12_c=50
#12abc=75 : Cannot start with a digit or Spaces are not allowed. Must Start with a letter or underscore_,
#Special characters also not allowed.
  #Identifiers: Identifiers are variables which are meaningful in nature.
"""name="Sachin"
age="30"
Price=20.5

#Case Sensitivity in Python:
   #Unicode represents a characters individual code representation in normal english
x=10
X=20
print(X)

a="Python"
b="python"
print(a==b) #Checks both case and value and return boolean response.

#String methods:
str1="sachinABC is a Student"
print(str1.upper())
x=str1.lower()
print(x)
print(str1.capitalize()) #First letter of first word will capitalize
print(str1.title()) #First letter of all keys get upper keys
print(str1.swapcase()) #Upper case will lower case and vice verza
print(str1.find("is")) #Returns the first position of a substring
print(str1.index("is")) #Returns the first position of a substring
print(str1.count("a")) #Count of particular word or character
print(str1.isupper()) #
print(str1.isdigit()) #Checks whether it is numbers

print(f"the original string is :{str1}")"""

#List Methods:

list1=[2,4,6,"sachin",3.5,7]
list1.append("place")
print(list1)
list1.pop()
print(list1)

list2=[3,4,"apple"]
list1.extend(list2)
print(list1)

list1.insert(0,"Orange")
print(list1)
list1.append(2)
list1.remove(2) #Removes only the first occurance of the element
print(list1)

print(list1.count(3))

# list1.clear()
# print(list1)

list1.reverse()
print(list1)

list3=list1.copy()
print(list3)

list4=[10,2.5,0,-10,100,.5]
list4.sort() #To convert in ascending order
print(list4)
list4.sort(reverse=True) #To convert in descending order
print(list4)

list5=["book","pen","Z","K","d","BOOK","PEN","Apple","aPPLE"]
list5.sort()
print(list5)

#Converts to alphabetical order first preference to Capital letter

#Methods: Append, Pop, copy, sort, reverse,remove,insert,extend,clear,Count

#Built in methods in Python List:

num=[2,5,6,7,10,12,100]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))

#Interview Question:
list6=[10,20,30,40]
name="apple"
#list6.insert(2,"apple")
list6.insert(2,name)
print(list6)
#expected output: list7=[10,20,"apple",30,40]

#------------------------------------------------------------------------
 #Tuple Methods:
num=(20,40,60,80,100,120,40,60)
print(num.count(40))
print(num.index(100))

#Create a tuple and add a new element in its second last index position
num=list(num)
num.insert(-2,50)
#In Python, when you use a negative index with insert(), the position is calculated relative to the end of the list, and the new element is inserted before the element at that calculated position.
print(num)
num=tuple(num)
print(num)

#Packing and unpacking of tuple
student=("sachin",30,"palakkad","male","kollam")
#name,age,place,gender=student
#print(name,age,place,gender)

student=["sachin",30,"Male","Palakkad","Kollam"]
name,age,gender,*place=student
print(name,age,gender,place)

tuple1=("a","b","c","D","E")
x,*y,z= tuple1
print(x,z)
print(y)

#Dictionary Methods:
dict1={"name":"Sachin","age":30,"gender":"Male"}
print(dict1["name"])
dict1["locaton"]="Palakkad"
print(dict1.get("name"))
dict1.update({"age":40})
print(dict1)
dict1["name"]="sach"
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#each key,value pair in a dictionary called as an items
