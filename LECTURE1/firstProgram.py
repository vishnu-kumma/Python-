
print("Vishnu")


# Primary DType :- 1.Integers   2.String    3.Float (True/False)    4.Boolean    5.None  -----------------

name = 'Bholenath'
print(type(name))  # <class 'str'>

salary = None
print(type(salary))   # <class 'NoneType'>



#  Keywords: Keywords are reserved words in python.
# and, def, del, assert, from, elif, etc.


# Print Sum

num1 = 5
num2 = 9
sum = num1 + num2
print("sum:",sum)

# OPERATOR --------------------------------------------------------------------------------------------------

# Arithmetic
x = 6
y = 2
print(x/y)      #    [3.0] always a float value even if operands are integer
print(x ** y)   #    36


# Relational : return boolean 
a = 10 
b = 20
print(a != b)    # True


# Assignment
z = 76
z += 10    #    or   z = z + 10  
print(z)


# Logical
print(not False)   #  True


# TYPE CONVERSION ----------------------------------------------------------------------------------------------------

# 1.Conversion : Automatically / implicit
a = 2
b = 4.25
sum = a + b   # 2.0 + 4.25 --> here int is automatically convetred into float [since float is superior(memory)] 



# 2.Casting : Manually

m = "2"      
n = 4.25

# print(m + n) # it will through error as we cant add these two . But we can forcefully converty them since automatical / implicit not possible

o = int("2")
p = 4.25
print(o + p)   # 6.25



# INPUT -> take input from user ---------------------------------------------------------------------------

name = input("Enter Your name: ")
print("Welcome",name)


value = int ( input("Enter your value: ")  )       # problem is the value would be string , So we will convert it into interger
print(type(value))

# WAP to input 2 floating numbers & print their average.

num1 = float (input("Enter 1st val: "))
num2 = float (input("Enter 2st val: "))
avg = (num1 + num2) / 2
print("Average: ",avg)


#  GITHUB ------------------------------------------------------------------------

# git init
# git remote add origin https://github.com/vishnu-kummar/Python-.git
# git add .
# git commit -m "Connecting local files to GitHub"
# git push -u origin main