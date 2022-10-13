# 첫번째 수 입력
n = int(input())
# 최대 개수의 수들을 저장할 리스트 
maxArr = []
# 최대 개수를 저장할 변수
temp = 0

# 두번째 수의 범위는 1 ~ n(n보다 크면 세번째 수는 바로 음수가 돼버림)
for i in range(1, n + 1):
    arr = [n, i] # 첫번째, 두번째 수 삽입
    a, b = 0, 1 # 앞의 앞의 수, 앞의 수 인덱스
    while True:
        if (arr[a] - arr[b]) < 0: # 음의 정수가 만들어 지면 중단
            break
        else: # 그렇지 않을 경우 만들어진 수를 리스트에 추가하고 인덱스 1씩 증가
            arr.append(arr[a] - arr[b])
            a += 1
            b += 1
    if len(arr) > temp: # 만들어진 수의 개수가 temp 보다 크면
        temp = len(arr) # temp 업데이트
        maxArr = arr[:] # maxArr 업데이트

print(temp)
print(' '.join(list(map(str, maxArr))))