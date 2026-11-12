#Input marks from the user:
"""marks>=90 grade is A
Marks>=80 grade is B
Marks>=70 grade is C
Marks>=60 grade is D
Marks<60 grade is fail
marks <0 and >100 is Invalid"""

"""marks=int(input("Enter your mark:"))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=90:
    print("Your grade is A")
elif marks>=80:
     print("Your grade is B")
elif marks>=70:
    print("Your grade is C")
elif marks>=60:
    print("Your grade is D")
else:
    print("FAILED") """

#Get the product first 10 natural numbers:
# product=1
# for i in range(1,11):
#     product*=i
# print(product)

#Get the sum of cubes of first 5 natural numbers.
# cubes=0
# for i in range(1,6):
#     cubes+=i**3
# print(cubes)

#Get the sum of cubes of first 10 even numbers.

cubes=0
for i in range(2,21,2):
    cubes+=i**3
print(cubes)
