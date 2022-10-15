# 종이의 가로, 세로 길이 입력
w, h = map(int, input().split())
# 잘린 길이가 들어갈 리스트(종이의 시작과 끝 인덱스는 미리 삽입)
width = [0, w] 
height = [0, h]

# 자르는 횟수 입력
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0: # 가로로 자르면
        height.append(b) # 세로 길이에 영향을 주니까 height에 삽입
    elif a == 1: # 세로로 자르면
        width.append(b) # 가로 길이에 영향을 주니까 width에 삽입

# 오름차순으로 정렬
width.sort()
height.sort()

# 가장 큰 사각형의 넓이
result = 0

for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        # 두 원소의 차를 이용해 잘린 사각형들의 넓이 계산
        x = width[i + 1] - width[i]
        y = height[j + 1] - height[j]
        # 넓이가 더 크다면 교체
        result = max(result, x * y)

print(result)