n = int(input())
data = []
for _ in range(n):
  data.append(int(input()))
data.sort(reverse=True)

weight = [] # 로프 갯수별 들 수 있는 최대중량을 저장할 리스트

for i in range(n):
  # 내림차순으로 정렬했기 때문에 로프의 최대 중량에 i + 1만큼 곱하면 됨
  # i번째 로프까지 사용했을때의 최대 중량을 각각 리스트에 추가
  weight.append(data[i] * (i + 1))
  
print(max(weight))

# 풀이 : https://jitolit.tistory.com/134