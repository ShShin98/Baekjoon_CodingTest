plane = [[0] * 101 for _ in range(101)] # 평면 생성
result = 0 # 사각형들이 차지하는 면적
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if plane[i][j] == 0:
                plane[i][j] = 1
                result += 1

print(result)