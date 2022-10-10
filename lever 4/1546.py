N = int(input())
L = list(map(int,input().split()))
avg = 0
for i in range(N):
  avg += L[i]/max(L)*100
print(avg/N)
# 여기서는 필요 없었지만 round(숫자, 소수점개수)로 소수점개수 제한가능