import math

stu = [[0, 0] for _ in range(7)] # 학년, 성별별 학생의 수를 저장할 리스트
room = 0 # 필요한 방의 개수
n, k = map(int, input().split()) # 학생의 수와 방의 최대 인원 입력

for _ in range(n): # 학년별로 리스트에 한명씩 추가
    s, y = map(int, input().split())
    stu[y][s] += 1

for i in range(1, len(stu)): # 0학년은 없으므로 1학년부터 반복
    room += math.ceil(stu[i][0] / k) + math.ceil(stu[i][1] / k)

print(room)