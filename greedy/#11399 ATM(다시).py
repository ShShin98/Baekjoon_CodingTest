n = int(input())
data = list(map(int, input().split()))
data.sort() # 오름차순으로 정렬

total = 0
sumData = 0

# i번째 원소까지의 합을 각각 sumArr 리스트에 저장
# i번째 사람이 돈을 인출하는데 걸린 시간 (앞사람들이 걸린 시간 + 자신이 걸린 시간)
for i in data:
  sumData += i 
  total += sumData

# 각 사람이 돈을 인출하는데 필요한 시간의 합 출력
print(total)