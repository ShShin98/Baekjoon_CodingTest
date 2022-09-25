n = list(input()) # 입력받은 문자열을 리스트 형태로 변경
n.sort(reverse=True) # 내림차순으로 정렬
sum = 0

# 각 자릿수를 더한 합
for i in n:
    sum += int(i) # 정수 형태로 변경해서 더함

# 30의 배수의 조건 : 각 자릿수를 더한 값이 3의 배수이고, 끝자리가 0일것
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))