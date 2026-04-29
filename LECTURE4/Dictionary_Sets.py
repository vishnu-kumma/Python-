
# DICTIONARY :- used to store data values in KEY:VALUE pair, They are unordered, mutable & don't allow duplicate keys.

dict = {
    "name" : "vishnu",
     "cgpa": 6.9,
     "marks": [67,89,58],
}

print(dict)                  # {'name': 'vishnu', 'cgpa': 6.9, 'marks': [67, 89, 58]}
print(dict["name"])          # vishnu
dict["name"] = "bholenath"   # mutable
dict["nickname"] = "Shivji"  # adding key-value 
print(dict)                  # {'name': 'bholenath', 'cgpa': 6.9, 'marks': [67, 89, 58], 'nickname': 'Shivji'}


# NOTE:  Empty dictionaryt can also be created -> dict = {} like this & then can add value as well like this -> dict["name"] = "xyz"

# NESTED DICTIONARY
student = {
    "name" : "abhinay",
    "score" : {
        "phy"  : 67,
        "che"  : 69,
        "maths": 79
    }
}

print(student["score"]["che"])   # 69
print(student["score"])          # {'phy': 67, 'che': 69, 'maths': 79}


# DICTIONARY METHODS

print(student.keys())       # returns all keys                          dict_keys(['name', 'score'])
print(student.values())     # returns all values                        dict_values(['abhinay', {'phy': 67, 'che': 69, 'maths': 79}])
print(student.items())       # returns all (key,value) pairs as tuples  dict_items([('name', 'abhinay'), ('score', {'phy': 67, 'che': 69, 'maths': 79})])

# list = list(student.items())  
# print(list[1])                # you can access using index by converting dictionary into list/tupples    

print(list(student.keys())) # return keys in the form of list           ['name', 'score']
print(len(dict))            # returns len. of dictionary

print(student.get("name"))   # returns  values according to key , if key is wrong then no error, "NONE" return
print(student["name"])       # returns  values according to key , if key is wrong then it will throw error


student.update({"city":"bihar","age":22})   # inserts the specified items to the dictionary



# SET :- Collection of unordered items. Each element in set must be unique & immutable(we can't change element value). 
# set is mutable as we are able to add / remove values. 
# NOTE:- you can store boolean, int, float, string, tuple in set but not list & dict. as they are mutable

collection = {1,2,3,4,3,"hello"}

print(collection)        # {1, 2, 3, 4, 'hello'} not {1, 2, 3, 4, 3, 'hello'} as it will not store duplicate eleement
print(len(collection))   # 5 instead of 6 i.e. ignored the duplicate value

# To create an empty set : collection = {} --> wrong . Correct one - collection = set() 


# SET METHOD

collection.add(69)    # adds  elelment 69 -> we can even add tuple -> collection.add((7,8,5)) but not list collection.add([3,4,5])
collection.remove(4)  # removes the element 4 in set if present , if not present then, throw error
collection.clear()    # empties the set
# collection.pop()      # removes a random value

set1 = {1,2,3,"a"}
set2 = {"a","b","c",1,3}
set3 = set1.union(set2)
print(set3)                # {1, 2, 3, 'c', 'a', 'b'} -> stored in unordered fashion . combines both set value & returns new one

set4 = set1.intersection(set2)
print(set4)               # {1, 3, 'a'}  . combines common values & returns new

 

