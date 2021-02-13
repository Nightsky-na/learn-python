a = int(input())
b = int(input())
c = int(input())

s = a + b + c


if s >= 80 and s <=100:
    print("A")
elif s >=75 and s <=79:
    print("B+")
elif s >= 70 and s <=74:
    print("B")
elif s >=65 and s  <=69:
    print("C+")
elif s >= 60 and s <=64:
    print("C")
elif s >=55 and s <=59:
    print("D+")
elif s >= 50 and s <=54:
    print("D")
elif s >= 0 and s <=50:
    print("F")
