students = int(input())
num = list(map(int, input().split()))
line = [1]

for i in range(1, students):
    pick = num[i]
    line.insert(len(line) - pick, i + 1)

for l in line:
    print(l, end=' ')