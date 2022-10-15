n = int(input())
switch = list(map(int, input().split()))
m = int(input())
student = []


def change(s):
    s = 0 if s == 1 else 1
    return s


for i in range(m):
    gen, a = map(int, input().split())
    if gen == 1:
        for i in range(len(switch)):
            if (i + 1) % a == 0:
                switch[i] = change(switch[i])
    else:
        s_index = a - 1
        change(switch[s_index])
        for i in range(1, len(switch)):
            if s_index - i < 0 or s_index + i >= n:
                switch[s_index] = change(switch[s_index])
                break
            elif switch[s_index - i] != switch[s_index + i]:
                switch[s_index] = change(switch[s_index])
                break
            elif switch[s_index - i] == switch[s_index + i]:
                switch[s_index - i] = change(switch[s_index - i])
                switch[s_index + i] = change(switch[s_index + i])
                
for i in range(n):
    if i >= 20 and i % 20 == 0:
        print()
    print(switch[i], end=' ')