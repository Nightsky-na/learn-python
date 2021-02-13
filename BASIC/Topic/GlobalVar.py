x = "awesome"

# @staticmethod
def myfunc():
    print("python is " + x + "\n")

myfunc()

y = "Jonh"
z = 5
w = 10
print(z + w) # print sum of z and w
# print(z + y) error 

# This function use for declar the var 
def myglobal():
    global  a
    a = "Hi, I'm Kontawat"

myglobal() #declar the variable a before use it
 
print("My name is " + a)