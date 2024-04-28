# Loops - are used to repeat instructions

# i = 1
# while(i < 10):
#     print("Messi")
#     i+=1
    
    
# j = 1
# while(j <= 10):
#     print(j)
#     j+=1
    
# x = 1
# while(x <= 10):
#     print(x*x)
#     x+=1
    
# table = int(input("Enter a number: "))
# z = 1
# while(z <= 10):
#     print(table*z)
#     z+=1


# nums = [1,4,9,16,25,36,49,64,81,100]

# index = 0
# while(index < len(nums)):
#     print(nums[index])
#     index+=1

# tup = (1,4,9,16,25,36,49,64,81,100)

# ind = 0
# target = 25
# while ind < len(tup):
    
#     if(target == tup[ind]):
#         print("Found at index",ind)
#     ind += 1

    
# Break & Continue

# Break - used to terminate the loop when encountered
# Continue - terminates execution in the current iteration & continue
# execution of the loop with the next iteration.

# i = 1 
# while i <= 10:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# j = 1 
# while j <= 10:
#     if j == 3:
#         j += 1
#         continue
#     print(j)
#     j += 1
    
    
    
# For Loop - used for sequential traversal.For traversing list,string,tuples etc.

# li = [1,2,3,4,5,6]

# for i in li:
#     print(i)
    
# li2 = ["leo","Messi","ronald","martinez"]

# for val in li2:
#     print(val)


# 1,4,9,16,25,36,49,64,81,100

# nums = [1,4,9,16,25,36,49,64,81,100]

# for el in nums:
#     print(el)
    
# nums = [1,4,9,16,25,36,49,64,81,100]

# target = 64
# index = 0
# for el in nums:
#     if(el == target):
#         print("Number found at index: ",index)
#     index+=1


# Range

# for i in range(5):
#     print(i)
    
# for j in range(5,10): # start,stop
#     print(j)
    
# for k in range(5,15,3): #start,stop,step
#     print(k)


# n = int(input("Enter your limit: "))

# i = 1
# sum = 0
# while(i <= n):
#     sum = sum + i
#     i +=1
    
# print(sum)


n = int(input("Enter your number: "))

i = n
fact = 1
while(i >=1):
    fact = fact * i
    i -=1
    
print(fact)