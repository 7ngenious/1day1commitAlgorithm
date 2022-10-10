N = int(input())
for i in range(N):
  # str = list(input()) 이렇게 했었는데
  # 굳이 리스트로 만들어 주지 않아도 됐다
  sum=0
  sum1 = 1
  for j in str:
    if(j == 'O'):
      sum += sum1
      sum1 += 1
    else:
      sum1 = 1
  print(sum)