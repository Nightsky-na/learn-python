import array
rows= int(input())
cols = int(input())
arr = []
arr2 = []
arr3 = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(int(input()))
    # arr.append(int(input()))
    arr.append(col)
# print(arr[1][2])

for i in range(cols):
    col = []
    for j in range(rows):
        col.append(int(input()))
    # arr.append(int(input()))
    arr2.append(col)

for i in range(rows):
    col = []
    for j in range(cols):
        col.append(arr[i][j] + arr2[i][j])
    arr3.append(col)

for i in range(cols):
    for j in range(rows):
        print(arr3[i][j])
        
