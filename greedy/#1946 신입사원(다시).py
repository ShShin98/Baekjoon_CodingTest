import sys

# 테스트 케이스 갯수 입력
T = int(sys.stdin.readline())

for _ in range(T): # 입력받은 테스트 케이스 횟수만큼
  people = [] 

  for i in range(int(sys.stdin.readline())): # 입력받은 지원자의 숫자만큼
    # 공백을 기준으로 구분하여 리스트에 추가
    people.append(list(map(int, sys.stdin.readline().split()))) 

  people.sort() # 서류 성적 순위대로 정렬 
  temp = people[0][1] # 서류 1등의 면접 등수 저장
  cnt = 1

  for i in range(1, len(people)): # 서류 2등부터 비교
    # (첫번째 반복) 서류 2등이 서류 1등보다 면접 등수가 높다면
    # 두번째 부터는 가장 최근에 합격처리된 사람과 비교
    if temp > people[i][1]:
      cnt += 1 # 합격처리
      temp = people[i][1] # 현재 사람의 면접 등수 저장
      # 면접 등수가 더 높아야 저장되기 때문에 항상 가장 높은 면접 순위가 저장
  
  print(cnt)

  # https://velog.io/@ledcost/백준-1946-파이썬-신입-사원-실버1-그리디
  # https://velog.io/@dding_ji/baekjoon1946