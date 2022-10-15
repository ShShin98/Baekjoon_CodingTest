n = int(input())
pillars = [] # 기둥 정보 입력받을 리스트
max_l = 0 # 가장 큰 l(가장 오른쪽 기둥의 위치)
max_h = 0 # 가장 큰 h(가장 높은 기둥의 높이)
max_h_index = 0 # 가장 높은 기둥의 위치

for _ in range(n):
    l, h = map(int, input().split())
    pillars.append([l, h]) # 기둥의 위치와 높이 추가
    if max_l < l: # 가장 오른쪽 기둥의 위치를 변수에 저장
        max_l = l
    if max_h < h: # 가장 높은 기둥의 높이, 위치를 변수에 저장
        max_h = h
        max_h_index = l

warehouse = [0] * (max_l + 1) # 창고 생성
for l, h in pillars: # 창고에 기둥 배치
    warehouse[l] = h

temp = 0
result = 0

for i in range(max_h_index + 1): # 왼쪽부터 가장 높은 기둥까지
    if warehouse[i] > temp: # 현재 기둥의 높이가 temp보다 높다면
        temp = warehouse[i]
    result += temp

temp = 0 # 오른쪽부터 비교하기 위해 0으로 초기화

for i in range(max_l, max_h_index, -1): # 오른쪽부터 가장 높은 기둥 전까지
    if warehouse[i] > temp: # 현재 기둥의 높이가 temp보다 높다면
        temp = warehouse[i]
    result += temp

print(result)

# 풀이 : https://namhandong.tistory.com/138