# In a way List & Tuples are like Array.
# LIST :- A built-in DType that stores set of values. Unlike array it can store element of different types (Integer, float, string etc.)
#         String & List are almost similar but string - immutable while list - mutable


marks = [45.9,76.3,78,40]
print(marks)                 # [45.9, 76.3, 78, 40]
print(marks[1])              # 76.3
print(type(marks))           # <class 'list'>
print(len(marks))            # 4
marks[2] = 69                # mutable
print(marks)                 # [45.9, 76.3, 69, 40]

student = ["Name",85,"Patna"]
print(student[1])            # 85



# LIST SLICING - similar to string slicing , ending index not included

num = [87,64,33,95,76]

print(num[1:4])                # 64,33,95
print(num[:4])                 # same as [0:4]         87,64,33,95
print(num[1:])                 # same as [1:len(num)]  64,33,95,76
print(num[-3:-1])              # 33 95



# LIST METHODS

li = [2,1,3]

print(li)                      # [2,1,3]
li.append(4)                   # add element at the last index [2,1,3,4]
li.sort()                      # sort in ascending order       [1,2,3,4]     . Note: charcater can also be sorted [a c b -> a b c] 
li.sort(reverse=True)          # sortss in descending order    [4,3,2,1]
li.reverse                     # reverse list                  1,2,3 --> 3,2,1 . It modifies the original list directly and returns None.
li.insert(2,10)                # insert 10 at index 2          [4, 3, 10, 2, 1]    
li.remove(1)                    # removes first occurence of given element       eg 2,1,3,1 --> 2,3,1 
li.pop(1)                      # remove element at index 1          [3,2,1]



# TUPLES -----------------------------------------------------------------------------------------------------
# A built-in DType that lets us create immutable(like string) sequences of values.

tup = (87,64,33,95,76)

print(tup)           # (87,64,33,95,76)
print(tup[1])        # 64
# tup[1] = 100       # ERROR as tuples is immutable


# NOTE- tup = () is valid & tup = (1,) is valid .Also if there's only 1 ele. write like this (3,) not (3) as it will consider as integer not tuple

# TUPLE SLICING is also possible.

# TUPLE METHODS

tupp = (2,1,3,1)

tupp.index(1)             # returns index of 1st occurrence  --> 1
print(tupp.count(1))      # count total occurrence           --> 2 



# Let's Practice ---------------------------
# WAp to ask the user to enter names of their 3 favourite movies & store them in a list.

# movies = []
# movie1 = input ("Enter 1st movie name : ")
# movie2 = input ("Enter 1st movie name : ")
# movie3 = input ("Enter 1st movie name : ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)


#----------------- WAP to check if a list contains a palindrome of elements. ----------------

# isPalindrome = [1, 2, 3, 21, 1]

# reversed_list = isPalindrome.copy()

# reversed_list.reverse()

# if reversed_list == isPalindrome:
#     print("Yes it is palindrome")
# else:
#     print("No it is not")



# ------------------- WAP to count no. of students with the "A" grade in following tuples ------------

# mark = ("C","D","A","A","B","B","A")
# print(mark.count("A"))







