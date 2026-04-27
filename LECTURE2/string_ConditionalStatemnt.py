
# # STRINGS: string is a data type that stores sequence of character.

# # Escape Sequence Character :- kuch special character jinka kaam hota hai formatting dena like | (tab\t), (next line\n) |

# str1 = "vishnu's"
# str2 = 'kumar'
# print(str1+str2)   # CONCATENATE -> vishnu'skumar

# print(len(str1))   # LENGTH    -> 8

# print(str1[3])     # INDEX     -> h  NOTE: you can only access using index not manipulate like str1[3] = h



# # SLICING :- parts of string .       NOTE:  end index is not include for e.g. str[1:3] here 3 is not included
# str = "ApnaCollege"
# print(str[1:4])     #                           --> pna
# print(str[:4])      # same as 0:4               --> Apna
# print(str[1:])      # same as str[1:len(str)]   --> pnaCollege
# print(str[-4:-2])   # -1 is for last index      --> le



# # STRING FUNCTIONS:- 
# stri = 'i am a coder.'

# print(stri.endswith("er."))       # returns true if string ends with substr
# print(stri.capitalize())          # capitalize 1st char. jo v changes ho rahe hai wo original me nhi, for orig. -> stri = stri.capitalize()
# print(stri.replace("i am","You")) # replace all occurences of old with new
# print(stri.find("a"))            # returns 1st index of 1st occurence
# print(stri.count("a"))           # counts the ocuurence of substr in string



# CONDITIONAL STATEMENT (if-elif-else)------------------------------------------------------------------------------------------

age = 17

if(age == 18):
    print("Can vote only")       # indentation to combine block of code not curly braces
elif(age > 18):
    print("can vote as well as drive")
else:
    print("ghare jake sutti babu")        


"""
Grade students based on marks
marks >= 90,      grade = "A"
90 > marks >= 80, grade = "B"
80 > marks >= 70, grade = "C"
70 > marks,       grade = "D"
"""    

# grade = int (input("Enter grade: "))

# if(grade >= 90):
#     print(grade,"--> A")
# elif(90 > grade >= 80):
#     print(grade,"--> B")
# elif(80 > grade >= 70):
#     print(grade,"-->C")
# else:
#     print(grade,"D")       


num1 = int(input("Enter 1st: "))
num2 = int(input("Enter 2nd: "))
num3 = int(input("Enter 3rd: "))

if(num1 > num2 and num1 > num3):
    print("num1")
elif(num2 > num1 and num2 > num3):
    print("num2")
else:
    print("num3")    





 

