# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split()) # 전체 보드의 크기 입력
board = [input() for _ in range(n)] # 보드 생성
cnt = [] # 다시 칠해야 하는 칸의 갯수를 저장

for i in range(n - 7): # 8 X 8 로 자를수 있는 시작점의 범위
  for j in range(m - 7): # 8 X 8 로 자를수 있는 시작점의 범위
    start_w = 0 # 첫번째 칸이 흰색일 경우 다시 칠해야 하는 횟수
    start_b = 0 # 첫번째 칸이 검은색일 경우 다시 칠해야 하는 횟수
    # 시작점을 기준으로 행, 열 8칸씩 체크
    for a in range(i, i + 8): 
      for b in range(j, j + 8):
        # 행 번호 + 열 번호가 짝수이면 첫번째 칸의 색과 같아야 함
        if (a + b) % 2 == 0:
          # 첫번째 칸이 흰색일 경우, 검은색일 경우 나눠서 체크
          if board[a][b] != 'W':
            start_w += 1
          if board[a][b] != 'B':
            start_b += 1
        # 행 번호 + 열 번호가 홀수이면 첫번째 칸의 색과 달라야 함
        else:
          # 첫번째 칸이 흰색일 경우, 검은색일 경우 나눠서 체크
          if board[a][b] != 'B':
            start_w += 1
          if board[a][b] != 'W':
            start_b += 1
    # 다시 칠해야 하는 횟수가 적은것을 저장
    cnt.append(min(start_w, start_b))  

# 최소 개수를 출력
print(min(cnt))

# 풀이 : https://bambbang00.tistory.com/43