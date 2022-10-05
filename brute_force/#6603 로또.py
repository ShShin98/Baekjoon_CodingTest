# https://www.acmicpc.net/problem/6603
from itertools import combinations

while True:
    arr = input().split() # str로 입력 (출력시 join을 하기 위해)

    if arr.pop(0) == '0': # 리스트의 맨 처음 값이 0이면 break
        break

    for com in combinations(arr, 6):
        print(" ".join(com))

    print()
