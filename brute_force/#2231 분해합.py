# https://www.acmicpc.net/problem/2231

n = int(input())
result = 0 # 가장 작은 생성자

# 입력받은 수만큼 반복
for i in range(n):
  sum_digit = 0 # 자릿수의 합
  for c in str(i): # i의 각 자릿수마다 반복
    sum_digit += int(c) # 자릿수 합 구하기
  sum = i + sum_digit # 분해합 구하기
  if sum == n: # 분해합이 n과 같다면
    result = i # i는 n의 생성자
    break

print(result)
