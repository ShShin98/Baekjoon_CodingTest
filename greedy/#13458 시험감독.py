n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = n

for i in a:
  forC = i - b

  if forC < 0:
    continue

  if forC % c == 0:
    result += forC // c
  else:
    result += forC // c + 1

print(result)