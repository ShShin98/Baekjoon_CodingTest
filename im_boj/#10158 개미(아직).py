w, h = map(int, input().split())
p, q = map(int, input().split())

# 북동, 북서, 남서, 남동 순
dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]
dir = 0

t = int(input())
cnt = 0

x, y = p, q

for i in range(t):
    x = x + dx[dir]
    y = y + dy[dir]

    if dir == 0:
        if x == w and y == h:
            dir = 2
        elif x == w:
            dir = 1
        elif y == h:
            dir = 3
    if dir == 1:
        if x == 0 and y == h:
            dir = 3
        elif x == 0:
            dir = 0
        elif y == h:
            dir = 2
    if dir == 2:
        if x == 0 and y == 0:
            dir = 0
        elif x == 0:
            dir = 3
        elif y == 0:
            dir = 1
    if dir == 3:
        if x == w and y == 0:
            dir = 1 
        elif x == w:
            dir = 2
        elif y == 0:
            dir = 1

print(x, y)