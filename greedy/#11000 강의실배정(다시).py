import heapq
import sys

n = int(input())

# [시작시간, 종료시간] 의 형식으로 리스트에 입력
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

data.sort() # 강의 시작시간이 빠른 순으로 정렬

room = []
# 첫번째 강의의 종료시간을 힙큐에 push
heapq.heappush(room, data[0][1])

# 두번째 강의부터 비교
for i in range(1, n):
  if data[i][0] < room[0]: # 새로운 강의의 시작시간이 현재 강의의 종료시간보다 빠르면
    heapq.heappush(room, data[i][1]) # 새로운 강의실 개설
  else: # 새로운 강의의 시작시간이 현재 강의의 종료시간보다 같거나 느리면 (강의실 이어서 사용 가능)
    # 기존 강의는 나오고 새로운 강의의 종료시간을 push
    heapq.heappop(room) 
    heapq.heappush(room, data[i][1])

print(len(room)) # 우선순위 큐에 남아있는 원소의 갯수가 결국 만들어진 강의실의 수 

# 우선순위 큐를 사용하는 이유 : 강의실을 이어서 사용하려면 종료시간이 가장 빠른 강의실을 찾아서 비교해야 하기 때문이다
# 자동으로 정렬상태를 유지하는 특성을 이용
# 풀이 : https://hongcoding.tistory.com/79