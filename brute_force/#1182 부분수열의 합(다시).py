# https://www.acmicpc.net/problem/1182
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    comb = combinations(arr, i)
    for a in comb:
        if sum(a) == s:
            cnt += 1

print(cnt)

# 풀이 : https://seongonion.tistory.com/98