# https://www.acmicpc.net/problem/7568
n = int(input()) # 전체 사람의 수 입력
# 사람의 수만큼 키와 몸무게 입력
arr = [list(map(int, input().split())) for _ in range(n)]

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

# 풀이 : https://claude-u.tistory.com/122