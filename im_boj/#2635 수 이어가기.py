# 첫번째 수 입력
n = int(input()) 
maxArr = []
temp = 0

for i in range(1, n + 1):
    arr = [n, i]
    a, b = 0, 1
    while True:
        if (arr[a] - arr[b]) < 0:
            break
        else:
            arr.append(arr[a] - arr[b])
            a += 1
            b += 1
    if len(arr) > temp:
        temp = len(arr)
        maxArr = arr[:]

print(temp)
print(' '.join(list(map(str, maxArr))))