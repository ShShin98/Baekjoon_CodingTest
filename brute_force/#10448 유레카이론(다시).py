# https://www.acmicpc.net/problem/10448

# 45번째 삼각수가 1035(그 이하의 삼각수를 저장)
tri = [i * (i + 1) // 2 for i in range(1, 46)]
# 3개의 삼각수의 합으로 이루어진 정수를 저장하는 배열
arr = [0] * 1001 

# 3개의 삼각수의 합 (모두 달라야 할 필요 없음) -> 3중 반복
for i in tri:
  for j in tri:
    for k in tri:
      num = i + j + k
      # 3개의 삼각수의 합이 1000 이하라면
      if num <= 1000:
        arr[num] = 1 # 리스트의 해당 위치를 1로 바꿈

t = int(input())
for _ in range(t):
  # 입력받은 수가 3개의 삼각수의 합으로 표현이 가능하면 배열의 해당 위치에는 1이 있다
  print(arr[int(input())])

# 풀이 : https://omins.tistory.com/30