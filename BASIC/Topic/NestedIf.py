#if ซ่อน if
age = int(input("ป้อนอายุคุณ : "))

if  age <= 15:
    if age ==15:
        print("ม.3")
    elif age == 14:
        print("ม.2")
    elif age == 13:
        print("ม.1")
    else:
        print("ประถม")
else:
    # print("ม.ปลาย")
    if age == 18:
        print("ม.6")
    elif age == 17:
        print("ม.5")
    elif age == 16:
        print("ม.4")
    else:
        print("มหาลัย")