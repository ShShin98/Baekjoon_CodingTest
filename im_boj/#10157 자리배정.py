c, r = map(int, input().split())
seats = [[0] * (r + 1) for _ in range(c + 1)]

k = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

x, y = 1, 1

for i in range(1, c * r + 1):
    if k > c * r:
        print(0)
        break

    if i == k:
        print(x, y)
        break

    seats[x][y] = i
     
    x = x + dx[dir]
    y = y + dy[dir]

    if x > c or y > r or x < 1 or y < 1 or seats[x][y]:
        x = x - dx[dir]
        y = y - dy[dir]
        dir = (dir + 1) % 4
        x = x + dx[dir]
        y = y + dy[dir]