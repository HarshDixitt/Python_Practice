# List - A built-in data type that stores a set of values.
    
# It can stores elements of different types(int,float,strings etc)


# Marks = [56,78,34.67,89.6]
# print(Marks)
# print(type(Marks))

# print(Marks[0])
# print(Marks[2])


# Student = ["Mohit" , 95 , 25 , "Jammu"]
# print(Student[0])
# print(Student[5]) # out of range

# List Methods

# list = [2,1,3.56]

# list.append(45)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# list.insert(1,23)
# print(list)
# list.remove(1)
# print(list)

#------------------------------------------------------------

# Tuple - a built-in data type that lets us create immutable sequences
    # of values.

# emptytup = ()
# print(type(emptytup))


# for single value tuple 

# t = (10,)
# print(t)
# print(type(t))

# Slicing in tuple

# tup2 = (1,2,3,4)
# print(tup2[:3])


# Methods in tuple

# tup = (87,64,23,78,34,34,24)
# print(type(tup))
# print(tup.index(87))
# print(tup.count(34))



# --------------------------------------------------------------------------------


# WAP to ask user to enter names of their 3 favorite movies & store them in a list

# mov1 = input("Enter 1 Movie name: ")
# mov2 = input("Enter 2 movie name: ")
# mov3 = input("Enter 3 movie name: ")

# list = []
# list.append(mov1)
# list.append(mov2)
# list.append(mov3)
# print(list)

# WAP to check if a list contains a pallindrome of elements 

# list = [1,2,3,2,1]
# list2 = list.copy()
# list2.reverse()
# print(list2)

# if(list2 == list):
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")
    
    
# WAP to count a number of students with the grade 'A' grade 
# in the following tuple 

# tup = ("B","A","B","A","B","A","C","A",'C')
# print(tup.count("A"))


# store the grade in the list and sort from A to C
list = ["B","A","B","A","B","A","C","A",'C']
list.sort()
print(list)
