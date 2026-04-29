
""" WAP to store following meanings in python dictionary:- 
    table : "a piece of furniture", "list of facts & figures"
    cat : "a small animal"
"""

dict = {
    "table" : [ "a piece of furniture", "list of facts & figures" ],
    "cat"   :   "a small animal"
}
print(dict)


#------------------------------------------------------------------------


""" You are given a list of subjecvts for student. Assume one classroom is required for 1 subject. How many
    classrooms are needed by all students.
    "python", "java", "C++", "python", "javascript", "java",
    "python", "java", "c++", "C"
"""

classroom = {"python", "java", "C++", "python", "javascript", "java","python", "java", "C++", "C"}
print(len(classroom))   # 5


#---------------------------------------------------------------------------


""" WAP to enter marks of 3 subjects from the user & store them in a dictionary. Start with an empty dictionary & add
    one by one. Use subject name as key & marks as value.

"""
dictionary = {}

m1 = int(input("Enter marks1 "))
m2 = int(input("Enter marks2 "))
m3 = int(input("Enter marks3 "))

dictionary.update({"phy":m1})
dictionary.update({"che":m2})
dictionary.update({"math":m3})

print(dictionary)




#--------------------------------------------------------------------------


"""
Figure out a way to store 9 & 9.0 as separate value in the set.
"""


sett = {9,'9.0'}
print(sett)

# OR

values = {
    ('float',9.0),
    ('int',9.0),
}
print(values)
