num = list(map(int, input()))
n_set = [0] * 10
result = 0

for n in num:
    if n == 6 or n == 9:
        if n_set[6] < n_set[9]:
            n_set[6] += 1
        else:
            n_set[9] += 1
    else:
        n_set[n] += 1

print(max(n_set))