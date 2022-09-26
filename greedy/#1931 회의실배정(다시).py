import sys

n = int(input())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 빨리 끝나는 순으로 정렬
# 끝나는 시간이 같다면 시작시잔이 빠른 순으로 정렬
data.sort(key=lambda x : (x[1], x[0]))

meeting = []

# 첫번째 회의의 끝나는 시간을 저장
endTime = data[0][1]

count = 1

# 두번째 회의부터 마지막까지 반복
for i in range(1, n):
  # 현재 회의 시작시간이 전 회의의 종료시간보다 같거나 크다면
  if data[i][0] >= endTime:
    endTime = data[i][1] # 현재 회의의 종료시간을 endTime에 저장
    count += 1 

print(count)
