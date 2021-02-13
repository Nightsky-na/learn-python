#same data type
#return => boolean

A = int(input("A is :"))
B = int(input("B is :"))
C = int(input("C is :"))

# เปรียบเทียบ 2 ตัวแปร
print("ค่า A > B หรือไม่ ? :", A>B)
print("ค่า A < B หรือไม่ ? :", A<B)
print("ค่า A = B หรือไม่ ? :", A==B)
print("ค่า A != B หรือไม่ ? :", A!=B)
print("ค่า A >= B หรือไม่ ? :", A>=B)
print("ค่า A <= B หรือไม่ ? :", A<=B)

# เปรียบเทียบ 3 ตัวแปร
print("ค่า A > B และ B > C หรือไหม ?:",A>B & B>C) 
print("ค่า A < B และ B < C หรือไหม ?:",A<B<C)

#Logical condition
"""
AND = และ
OR = หรือ
NOT = ไม่

Answer will be boolean
"""
D = (A > B)
E = (A == B)
print(type(D))
print(type(E))

# F = (A > B) and (A == B)
F = D and E
print(F)
print(not F)