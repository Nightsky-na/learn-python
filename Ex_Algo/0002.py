import array 
a = []
n  = int(input())

for i in range(n):
    a.append(int(input()))
max = a[0]
min = a[0]
for x in a:
    if(x > max):
        max = x
    elif(x<min):
        min = x
print(min)
print(max)       