# if elif else 
"""
i = 1

while i:
    age = int(input("Type your num : "))
    if age >= 15:
        print("นาย")
        i = 0
    elif age <=15 and age > 0:
        print("เด็กชาย")
        i = 0
    else:
        print("Reupload age")
        i = 1
"""

'''
if boolen expression:
    statement

'''
"""
age = int(input("Type your age : "))

if age >= 0 and age <15:
    print("วัยเด็ก")
elif age >= 15 and age <= 20:
    print("วัยรุ่น")
elif age > 20 and age <= 60:
    print("วัยผู้ใหญ่")
elif age > 60:
    print("วัยชรา")
else:
    print("กรอกใหม่น้าาาา")
"""
age = int(input("Type your age : "))

if age >=15:
    print("วัยรุ่น")
else:
    print("วัยเด็ก")

#"เงื่อนไขเป็นจริง" if expression else "เงื่อนไขอิ่นๆ"

print("วัยรุ่น") if age>=15 else print("วัยเด็ก")
