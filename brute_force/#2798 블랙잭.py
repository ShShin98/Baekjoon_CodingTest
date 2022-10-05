# https://www.acmicpc.net/problem/2798
from itertools import combinations

n, m = map(int, input().split()) # 카드의 개수와 m 입력
cards = list(map(int, input().split())) # n장의 카드 입력
comb = list(combinations(cards, 3)) # 3장의 카드를 뽑는 조합
sumArr = [] # 카드의 합을 저장할 리스트

for c in comb: # 3장의 카드를 뽑는 조합마다 반복
    if sum(c) <= m: # 3장의 카드의 합이 m 이하라면
        sumArr.append(sum(c)) # 리스트에 추가

print(max(sumArr)) # 리스트에서 가장 큰 값을 출력