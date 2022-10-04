# https://www.acmicpc.net/problem/2503
from itertools import permutations

# 1 ~ 9 에서 서로 다른 3개의 숫자를 뽑아 만든 순열 생성 (가능한 범위의 숫자들을 미리 생성)
num = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))

n = int(input())

for _ in range(n):
    guess, strike, ball = map(int, input().split())
    removed = 0  # 리스트 인덱스를 맞춰주기 위한 변수
    guess = list(str(guess))  # 비교를 위해 문자열 형태로 변환

    # 생성한 순열의 개수만큼 반복
    for i in range(len(num)):
        sCnt, bCnt = 0, 0
        i -= removed  # 후보가 아닌 숫자가 리스트에서 삭제되기 때문에 인덱스를 항상 0으로 고정해야함
        # i가 계속 증가하기 때문에 removed도 같이 증가시킨다음 i에서 빼주는것
        for j in range(3):  # 숫자가 세자리이기 때문
            guess[j] = int(guess[j])
            if guess[j] in num[i]:  # 질문한 숫자의 j번 인덱스의 숫자가 num의 i번째 튜플에 있는가
                if j == num[i].index(guess[j]):  # 위치도 같으면 스트라이크 횟수 1 증가
                    sCnt += 1
                else:  # 위치는 다르지만 있다면 볼 횟수 1 증가
                    bCnt += 1
        # 질문한 숫자의 스트라이크, 볼의 개수와 순열을 통해 얻은 스트라이크, 볼 개수가 다르면
        if sCnt != strike or bCnt != ball:
            num.remove(num[i])  # 후보지에서 제외
            removed += 1

print(len(num))

# 풀이 : https://omins.tistory.com/23