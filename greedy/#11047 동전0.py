n, k = map(int, input().split())
data = [0] * n

for i in range(n):
  data[i] = int(input())
data.sort(reverse=True)

result = 0

for coin in data:
  result += k // coin
  k = k % coin

print(result)