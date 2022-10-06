# N = int(input())
# sum = int()#값의 형식을 초기화해주고 사용해야하구나
# for i in range(N):
#   sum = sum+N
#   N= N - 1
# print(sum)  
# 좋은코드는 아님
N = int(input())
sum = 0
for i in range(1,N+1):
  sum += i
print(sum)