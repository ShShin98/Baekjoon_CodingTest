board = []

row = [0] * 5
column = [0] * 5
left_diag = 0
right_diag = 0

cnt = 0
line = 0

for _ in range(5):
    board.append(list(map(int, input().split())))

call = (list(map(int, input().split())))
for _ in range(4):
    call += list(map(int, input().split()))

for c in call:
    cnt += 1
    for n in range(5):
        for m in range(5):
            if c == board[n][m]:
                row[n] += 1
                column[m] += 1
                if row[n] == 5:
                    line += 1
                if column[m] == 5:
                    line += 1
                if n == m:
                    left_diag += 1
                    if left_diag == 5:
                        line += 1
                if (n == 0 and m == 4) or (n == 1 and m == 3) or (n == 2 and m == 2) or (n == 3 and m == 1) or (n == 4 or m == 0):
                    right_diag += 1
                    if right_diag == 5:
                        line += 1
    if line >= 3:
        print(cnt)
        break