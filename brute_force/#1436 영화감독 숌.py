end_num = [0] * 10001 # 1~10000번째 종말의 숫자 저장
num = 666 # 첫번째 종말의 숫자
i = 1 # 리스트 인덱스 카운트

while True:
  if '666' in str(num): # 숫자에 666이 포함되어있으면
    end_num[i] = num # 해당 숫자를 리스트에 저장
    i += 1 # 인덱스 1 증가
  num += 1 # 숫자 1증가
  if i == 10001: # 리스트가 다 차면 탈출
    break

print(end_num[int(input())]) 