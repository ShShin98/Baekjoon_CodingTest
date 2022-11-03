n = int(input())

w = 0  # 긴 변의 가로길이
w_index = 0 # 긴 변의 가로길이의 인덱스
h = 0  # 긴 변의 세로길이
h_index = 0 # 긴 변의 세로길이의 인덱스

arr =  [] # 변의 방향과 길이를 저장
for i in range(6):
    dl = list(map(int, input().split()))
    arr.append(dl)
    if dl[0] == 1 or dl[0] == 2: # 방향이 동 or 서 일때(가로)
        if w < dl[1]: # 긴 가로변의 길이와 인덱스를 저장
            w = dl[1]
            w_index = i
    elif dl[0] == 3 or dl[0] == 4: # 방향이 남 or 북 일때(세로)
        if h < dl[1]: # 긴 세로변의 길이와 인덱스를 저장
            h = dl[1]
            h_index = i

# 긴 가로변과 맞닿은 세로변의 차이가 작은 사각형의 세로 길이가 됨 (세로변도 동일)
small_w = abs(arr[h_index - 1 if h_index > 0 else 5][1] - arr[h_index + 1 if h_index < 5 else 0][1])
small_h = abs(arr[w_index - 1 if w_index > 0 else 5][1] - arr[w_index + 1 if w_index < 5 else 0][1])

area = w * h - small_w * small_h
result = area * n

print(result)

# 풀이 : https://itcrowd2016.tistory.com/m/84