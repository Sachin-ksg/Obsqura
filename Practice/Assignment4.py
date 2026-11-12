#String based questions:
#1.check whether the given character is a vowel or not (input: x="A")
# vowles="aeiouAEIOU"
# x=input("Enter a Character:")
# if x in vowles:
#     print("Character is vowel")
# else:
#     print("Not a vowel ")

#2.check whether the given character is a consonant or vowel:
# vowles="aeiouAEIOU"
# char=input("Enter a Character:")
# if char in vowles:
#     print("Character is vowel")
# else:
#     print("Character is Consonant ")


#3.Count the number of vowels in a user input (x="python")
# vowels="aeiouAEIOU"
# x="python"
# count=0
# for i in x:
#     if i in vowels:
#         count+=1
# print(count)

#4.Count the number of vowels in a user input (x="python is easy to learn")

# vowels="aeiouAEIOU"
# x="python is easy to learn"
# count=0
# for i in x:
#     if i in vowels:
#         count+=1
# print(count)

#Loop Based questions:
#1.Get the count of multiples of 5 from the below list (input: x=[1,5,10,15,8,4])
# count=0
# x=[1,5,10,15,8,4]
# for i in x:
#     if i%5==0:
#         count+=1
# print(count)

#2.Identify the most repeated element in the given list. List=[5,10,5,10,5,3,2]


max_count=0
most_repeated=0
lis=[5,10,5,10,5,3,2]
for i in lis:
    count=lis.count(i)
    if count>max_count:
        max_count=count
        most_repeated=i
print(most_repeated)



    
#3.Count the number of strings from the below list : List=[5,10,"A","Python","Hello",3.5,False]
# count=0
# lis = [5, 10, "A", "Python", "Hello", 3.5, False]
# for i in lis:
#     if type(i)==str:
#         count+=1
# print(count)