import itertools

array = [int(input()) for _ in range(9)]

for i in itertools.combinations(array, 7):
  if sum(i) == 100:
    for j in sorted(i):  # 그 7명을 오름차순으로 정렬후 출력한다.
      print(j)
    break