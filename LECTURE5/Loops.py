
# LOOPS are used to repeat instructions.


                                           # WHILE LOOP
# will print 1 - 5
# num = 1
# while num <= 5:
#     print(num)            
#     num += 1


# # will print 5 - 1
# x = 5
# while(x != 0):
#     print(x)              
#     x -= 1    


# PRINT TABLE    
# x = 7
# y = 1
# while (y <= 10):
#     print(x * y)
#     y += 1


# PRINT THE ELEMENT OF LIST USING LOOP 
# list = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(list):
#     print(list[idx])
#     idx += 1


# SEARCH FOR A NUMBER X IN THIS TUPPLE USING LOOP
# tup = (1,4,9,16,25,36,49,64,81,100)

# i = 0
# x = 64
# while i < len(tup):
#     if(tup[i] == x):
#         print("Found at index - ",i)
#     i += 1


# BREAK & CONTINUE ----------------------------------------------------------------

# BREAK    - used to terminate the loop when encountered.
# m = 0
# while(m < 5):
#     if(m == 3):
#         break
#     print(m)       # 0 1 2 not 3 4 
#     m += 1


# CONTINUE - terminates execution in the current iteration & continues execution of the loop with the next iteration. 
# n = 1
# while(n <= 10):
#     if(n % 2 == 0):
#         n += 1
#         continue    # 1 3 5 7 9 [skips]
#     print(n)
#     n += 1



                                           # FOR LOOP - Used for sequential traversal. For traversing list, string, tuples etc.

# nums = [2,4,3,5,9,"potato"]
# for i in nums:
#     print(i)


# str = "vishnuKumar"
# for i in str:
#     print(i)    


# Print the elements of LIST using FOR loop.
# li = [1,4,9,16,25,36,49,64,81,100]
# for i in li:
#     print(i)

# Search for a number x in this tupple using FOR loop
# tu = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# for i in tu:
#     if(i == x):
#         print("FOUND ")
#         break
#     else:
#         print("searching")


#----------------------------------------------------------------------------------------------------------------------------------------
# RANGE() - range fun. return a sequence of num., starting from 0 by default, & increment by 1(by default), & stop before a specified number.
# for e.g. range(5) -> gives -> 0 1 2 3 4

seq = range(5)
# print(seq[0])  
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])
# print(seq[5]) ->  throw error
#                                     OR print using loop

# for i in seq:
#     print(i) 
#                                     OR simple write range in loop

# for i in range(5):
#     print(i)


# NOTE:- syntax:-  range( start?, stop, step? ) where start & step is optional


# for i in range(10):       # range(stop)
#     print(i)              # 0 1 2 3 4 5 6 7 8 9

# for i in range(2, 10):    # range (start,stop)
#     print(i)              # 2 3 4 5 6 7 8 9

# for i in range(2, 10, 2): # range (start,stop,step)
#     print(i)              # 2 4 6 8


# PASS STATEMENT - pass is a null statement that does nothing. It is used as a placeholder for future code.

# for i in range(5):
#     # empty         --> here i wanted to implement this work but not know but it will throw error. solution -> see below code
# print("some useful work")    


# for i in range(5):
#     pass
# print("some useful work")

