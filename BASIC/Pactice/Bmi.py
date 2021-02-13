# โปรแกรม คำนวณ BMI
weight = float(input("Type your weight(kg) : "))
height = float(input("Type your height(cm) : "))

#cm -> m
height /= 100 
#cal BMI
bmi = (weight / height**2)

print("Your BMI is", bmi)

if bmi < 18.0:
    result = "ต่ำกว่าเกณฑ์"
elif bmi>= 18.0 and bmi< 23.0:
    result = "สมส่วน"
elif bmi >= 23.0 and bmi <= 25:
    result = "น้ำหนักเกิน"
elif bmi > 25.0 and bmi < 30.0:
    result = "โรคอ้วน ระดับที่1"
elif bmi >= 30.0:
    result = "โรคอ้วนอันตราย"
else :
    result = "ไม่ทราบค่า"

print("ํYour BMI is ", bmi ," ทำนายว่า ",result)