# Collection datatypes / data structures - can store multiple values in a single variable
# List , Tuple, Set, Dictionary
x = list()
print(x)
x = [10, 20.8, False, 'Sachin', 10, 10]
print(x)
# List features - Ordered, Duplication allowed, Mutable, Indexing, Slicing
print(x[0])
print(x[2])

print(x[0:3])  # collects the elements indexes 0,1,2
y=x[2:6]
print(y)

length_x=len(x)
print(length_x)

print(x[0:])
print(x[:6])
print(x[:])
print(x[0:6:2])
# slicing syntax [starting index : ending index+1 : step]

x = [10, 20.8, False, 'Sachin', 10, 10]
print(x[-3])
print(x[-5:-2])  #collects the elements in indexes -5,-4,-3


#TUPLE - It is the unmutable collection data structure in Python
x=tuple()
print(type(x))
print(x)

x=(12,10.7,True, "Sachin",10,10,[2,4,6],(100,200))
print(x)

#Tuple features: Ordered, duplication allowed, indexing , slicing, multi data storage
 # tuple is fatser than List in case of large number of data- as it is unmutable.

#Set:
x=set()
print(x)
print(type(x))
x={4} #empty curly braces will note dictionary , at least one value required to make it set
print(type(x))

x={2,3.5,"sachin",True,10,10}
print(x)
#Set Features - unordered, no duplicates, no indexing, no slicing, mutable, cannot add list or tuples

#Dictionary: The only named index data structure in Python.

x=dict()
x={"name":"Sachin","Age":30,"Gender":"Male","name":"Suresh","contact":[123,456,789]}
print(x)
print(x["Age"])
print(x["contact"])
print(x["contact"][0])
print(x["contact"][1])

#Dictionary features : ordered, changeable/mutable and do not allow duplicates
