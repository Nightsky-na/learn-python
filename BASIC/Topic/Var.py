from typing import Collection


x = 5 # x is int 
y = "Kontawat" # y is string
z = 3.0
print(x)
print(y)
print(z,"\n")

w = str(3) # w will be '3'
m = int(3) # y will be 3
n = float(3) # z will be 3.0
print(w)
print(m)
print(n,"\n")

print("x is", type(x))
print("m is", type(m), "\n", "\n")

"""""""""""""""""""""""""""""""""""""""""""""
 String can declare in 2 way "Meng" / 'Meng'
"""""""""""""""""""""""""""""""""""""""""""""
a = "Meng"
b = 'Meng'

print(a) 
print("a is", type(a))
print(b) 
print("b is", type(b),"\n")

d, e, f = "Orenge", "Banana", "Cherry"
print(d)
print(e)
print(f, "\n")

"""""""""""""""""""""""""""""""""""""""""""""
             Unpack a Collection
"""""""""""""""""""""""""""""""""""""""""""""
subject = ["Digital", "Java", "English"]
dig, ja, eng = subject
print(dig)
print(ja)
print(eng)

print("Hard subject is " + dig +" "+ ja +" "+ eng + ".")
