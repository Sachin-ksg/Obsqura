#Arithmatic operators: + , - ,* ,%, / , // ,**

"""a,b=10,20
print(a+b) #30
print(a-b) #-10
print(a*b) #200
print(a/b) #0.5 - normal division
print(a//b) #0 -floor division
print(a%b) #10 -remainder- modular division
print(a**2) #base **exponent

a,b="hello"," sachin"
print(a+b) #concatenation: adding two strings

a,b=10, "hello"
print(a+b) """

"""#Comparison operator: >,< ,<=,>=,=,==, != (returns a boolean value)
a,b=20,"20"
#print(a>b)
#print(a<b)

print(a==b) #It will checks both the value and data types where equal or not.
print(a!=b)"""

"""#Assignment operators:
a,b=10,20
a=a+b
print(a)

a,b=10,20
a+=b #a-=b, #a*=b possible for all arithmetic operations
print(a)"""

"""#Logical Operators: and , or ,not (returns boolean value)
a,b,c=10,20,30
print(a<b and b<c and c>a)
print(a<b and b>c and c>a) #and operator : returns true if all conditions are true

print(a<b or b<c or c>a) #or operator: if any one of the condition is true , returns true

print(not b>c) #To handle the reverse case."""

#Membership operator: in , not in
a="hello"
print("o" in a)
print("O" in a)

b=[10,20,30,40]
print(50 not in b)

#Identity operators: is, is not (equal as == ,!=)

a,b=10,20
print(a is b)
print(a is not b)