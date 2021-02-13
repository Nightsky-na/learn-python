#Type conversion
x = 10
y = 3.14
z = "20"
print(type(x))
print(type(y))
print(type(z))
#บวกเลข
result = x+y #10 + 3.14 = 13.14

# = x + z ไม่ได้ string + เลขไม่ได้

#String => int "20" => 20
int(z) # แปลงชนิด ได้เลย
sum = int(z) + x

#Int => String 10 => "10"
con = str(x) + z # str + str => cat
# "10" + "20" => "1020"

#String => float
sumFloat = float(z) + y

#float => string
conString = str(y) + z

print(int(y))

z = float(z)
x = float(x)
y = str(y)

print(type(x))
print(type(y))
print(type(z))

print(result)
print(sum)
print(con)
print(sumFloat)
print(conString)
