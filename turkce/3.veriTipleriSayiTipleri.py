"""
this is a comment
written in more
than just one line
"""

print("Welcome to turkey")


print(type(1.5)) #<class 'float'>

print(3 + 4) #7

print(5%3) #2

print(3 + 2 * 5) #13
print(3 + (2 + 8) * 2 + 4) #27

print(3.5 * 4 / 2.1) #6.666666666666666

print("-------------------")

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)  #Sally

print("--------------------")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x , y , z) #3 3 3.0

print("------------------------------------")

x = 5
y = "John"
print(type(x)) #<class 'int'>
print(type(y)) #<class 'str'>

print("-----------------------------------------------")

x = "John"
# is the same as
x = 'John'
print(type(x)) #<class 'str'>
print(x)

print("---------------------------------------")

a = 4
A = "Sally"
#A will not overwrite a
print(a) #4
print(A) #Sally
