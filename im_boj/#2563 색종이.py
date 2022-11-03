board = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if board[i][j] == 0:
                board[i][j] = 1
result = 0
for a in board:
    for b in a:
        if b == 1:
            result += 1

print(result)