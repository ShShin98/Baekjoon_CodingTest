plane = [[0] * 1001 for _ in range(1001)]
n = int(input())

for num in range(1, n + 1):
    x, y, width, height = map(int, input().split())

    for i in range(x, x + width):
        for j in range(y, y + height):
            plane[i][j] = num

for i in range(1, n + 1):
    cnt = 0
    for j in range(1001):
        cnt += plane[j].count(i)
    print(cnt)