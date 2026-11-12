"""In file handling , for testing purpose the most commonly used files are txt,json and excel
"""
#txt file:
#using built-in open() function
#Opening files in read mode
# file=open("data.txt","r")
# content=file.read()
# print(content)

file1=open("data.txt","r")
content=file1.readlines()
print(content)

file1=open("data.txt","r")
content=file1.readline()
print(content)

#opening files in write mode:

# new_file=open("data.txt","w")
# new_file.write("hello")

new_file=open("data1.txt","w")
new_file.write("name:arun")

#opening file in append mode:
file=open("data.txt","a")
file.write("contact:456789 \n")
new_file.close()
print(new_file.closed)

#Methods applicable in existing file: read, write, append, create
#Methods applicable in non existing file: write(w), append(a), create(x)

#File handling using with statement:
"""with statement automatically closes the file when the block finishes, even if an exception occurs"""
with open("data.txt","r") as file1:
  content=file1.read()
  print(content)
  print(file1.closed)
print(file1.closed)

