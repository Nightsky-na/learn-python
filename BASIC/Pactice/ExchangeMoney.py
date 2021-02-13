money = int(input("ใส่จำนวนเงินของคุณ : "))

if money >= 1000:
    print("1000 บาท = ",money//1000)
    money %= 1000
if money >= 500:
    print("500 บาท = ",money//500)
    money %= 500
if money >= 100:
    print("100 บาท = ",money//100)
    money %= 100
if money >= 50:
    print("50 บาท = ",money//50)
    money %= 50
if money >= 20:
    print("20 บาท = ",money//20)
    money %= 20
