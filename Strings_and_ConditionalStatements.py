# Strings 

# str1  = 'This is string 1'
# str2 = " This is string 2"
# str3 = """ This is string 3"""


# print(str1 + str2 + str3)

# college = "IIIT \nHyderabad"
# # \n is escape sequence which is used for formatting
# print(college)
# print(len(college))


# Indexing 

# Name = "Leo Messi"
# print(Name[5])

# While using Indexing we can only access not modify/manipulate.

# Slicing - Accessing parts of a string

# str = "Greatest of all time"

# print(str[0:6])

# print(str[:])

# print(str[4:len(str)])

# SLicing - using negative index

# A   P  P  L  E
# -5 -4 -3 -2 -1

# str_1 = "Apple"

# print(str_1[-3:-1])

# string functions




# str = "i am learning python language"

# print(str.endswith("ge"))

# capitalstr = str.capitalize()
# print(capitalstr) 

# print(str.replace("learning", "enjoying"))

# print(str.find("language"))

# print(str.count("a"))


# CONDITIONAL STATEMENTS

# age = 21
# if(age >=18):
#     print("You can vote")
# else:
#     print("Not eligible")
    
    
# light = "Green"

# if(light == "Red"):
#     print("Stop")
# elif(light == "Green"):
#     print("Gooo")
# elif(light == "yellow"):
#     print("Look")
# else:
#     print("Light is not functioning")
    
# Grade students based on marks

# Marks = int(input("Enter Student Marks: "))
# if(Marks >= 90):
#     print("Grade A")
# elif(Marks >= 80 and Marks < 90):
#     print("Grade B")
# elif(Marks >= 70 and Marks < 80):
#     print("Grade C")
# else:
#     print("Grade D")
    
# WAP to check num is odd or even

# num = int(input("Enter Your Number "))
# if(num % 2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")

# Greatest b/w 3 numbers

# a = int(input("Enter Your Number "))
# b = int(input("Enter Your Number "))
# c = int(input("Enter Your Number "))
# if(a > b and a > c):
#     print(a," is greater")
# elif(b > a and b > c):
#     print(b," is greater")  
# else:
#     print(c," is greater")

# If a num is a multiple of 7 or not

num = int(input("Enter Your Number "))

if(num % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a multiple")