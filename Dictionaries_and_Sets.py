# Dictionary in Python are used to store data values in key:value pairs

# They are unordered , mutable & don't allow duplicate keys.

# List ko nhi le skte bcz it is mutable

# dict = {"name" : "Messi","CGPA" : "8.1","Marks" : [92,39,12]}

# print(dict)
# print(type(dict))

# print(dict["name"])

# dict["name"] = "Lionel"
# dict["CGPA"] = "8.6"
# print(dict)


# null_dict = {}
# print(null_dict)


# Nested Dictionaries

# student = {
#     "name" : "Rohit",
#     "Subjects" : {
#         "Phy" : 56,
#         "Chem" : 67,
#         "Maths" : 89
#     }
# }

# print(len(student))
# print(student)

# print(student["Subjects"])

# print(student["Subjects"]["Phy"])
# print(student["Subjects"]["Chem"])
# print(student["Subjects"]["Maths"])

# Dictionary Methods

# returns all keys
# print(student.keys())

# # returns all values
# print(student.values())

# # returns all (key , val) pair as tuples
# print(student.items())

# # returns the key according to value
# print(student.get("Subjects"))

# # inserts the specified itrms in dictionary
# student.update({"City" : "New Delhi"})
# print(student)


#---------------------------------------------------------


# Sets in Python - is the collection of the unordered itrms.

# Each element in the set must be unique & immutable.


# Note: Sets are mutable but elements of set are immutable

# set1 = {1,2,3,4,"hello","world","python"}

# print(type(set1))

# print(len(set1)) # total no of items and duplicate items are ignored


# null_set = {} # empty dictionary

# print(type(null_set))

# null_set1 = set() # this is empty set

# print(type(null_set1))


# set2 = {1,2,3,4,5,6}

# set2.add(7)
# set2.add("Messi")
# print(set2)
# set2.remove(6)
# print(set2)

# set2.pop() # random order values are popout 
# set2.pop()
# print(set2)

# print(len(set2))

# set2.clear()
# print(len(set2))


# set3 = {1,2,3,4}
# set4 = {2,3,4,5}

# print(set3.union(set4))

# print(set3.intersection(set4))


# -------------------------------------------------------


# store following word meanings in a python dictionary

# dict = {
#     "cat" : "a small animal",
#     "table" : ("a peice of furniture","list of facts & figures")
# }

# print(dict)


# You are gien a list of subjects for students.Assume one classroom
# is required for 1 subject.How many classrooms are needed by all students

# "python","java","c++","python","c++","python","java","java"


# set = {"python","java","c++","python","c++","python","java","java"}

# print(len(set))

# WAP to enter 3 sub marks and store them in dictionary

# marks = {}

# x = int(input("Enter Physics marks: "))
# marks.update({"Phy":x})
# y = int(input("Enter Chemistry marks: "))
# marks.update({"Chem":y})
# z = int(input("Enter Mathematics marks: "))
# marks.update({"Maths":z})

# print(marks)


# figure out a way to store 9 and 9.0 as seperate values in the set,

set = {4,"4.0"}
print(set)