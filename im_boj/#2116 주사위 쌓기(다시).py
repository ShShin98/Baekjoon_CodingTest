n = int(input())
dice = []
# 주사위의 아랫면에 따른 윗면의 인덱스(A:0 B:1 C:2 D:3 E:4 F:5)
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

for _ in range(n):
    dice.append(list(map(int, input().split())))

# 최대값을 저장해줄 변수
result = 0

for i in range(6): # 첫번째 주사위의 모든 면마다
    side_max = [] # 옆면의 최댓값을 저장할 리스트
    temp = [1, 2, 3, 4, 5, 6] # 주사위 각 면의 숫자
    temp.remove(dice[0][i]) # 주사위 아랫면의 숫자 제거
    next = dice[0][rotate[i]] # rotate를 통해 주사위 윗면의 인덱스를 알아냄 -> 윗면의 숫자 알아냄
    temp.remove(next) # 주사위 윗면의 숫자 제거
    side_max.append(max(temp)) # 남은 숫자(옆면)들 중 가장 큰 수를 리스트에 추가
    for j in range(1, n): # 두번째 주사위부터 마지막 주사위까지 반복
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(next) # 현재 주사위의 아랫면(전 주사위의 윗면과 같음)의 숫자 제거
        # 현재 주사위의 아랫면의 인덱스(next의 인덱스)를 알아내서 rotate를 통해 윗면의 인덱스를 구함
        next = dice[j][rotate[dice[j].index(next)]] # 알아낸 인덱스를 통해 윗면의 숫자 계산
        temp.remove(next) # 주사위 윗면의 숫자 제거
        side_max.append(max(temp)) # 남은 숫자(옆면)들 중 가잔 큰 수를 리스트에 추가
    result = max(result, sum(side_max))
        
print(result)

# 풀이 : https://velog.io/@sangjin98/알고리즘파이썬-백준-2116번-주사위-쌓기