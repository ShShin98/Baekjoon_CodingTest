n = int(input())
arr = list(map(int, input().split()))

cnt_plus = 1
cnt_minus = 1
result = 1

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        cnt_plus += 1
    else:
        cnt_plus = 1
    result = max(result, cnt_plus)

for i in range(1, n):
    if arr[i] <= arr[i - 1]:
        cnt_minus += 1
    else:
        cnt_minus = 1
    result = max(result, cnt_minus)

print(result)