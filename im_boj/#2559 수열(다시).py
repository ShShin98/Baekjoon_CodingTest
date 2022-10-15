import sys

n, k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

# 0번부터 슬라이싱한 합을 미리 저장
temp = sum(arr[:k])
result = [temp]

for i in range(n - k):
    # 전의 합에서 맨 앞의 값을 빼고 맨 뒤의 다음 값을 더해줌
    # 이렇게 하지 않고 매번 슬라이싱 후 sum을 해버리면 시간 초과
    temp = temp - arr[i] + arr[i + k]
    result.append(temp)

print(max(result))