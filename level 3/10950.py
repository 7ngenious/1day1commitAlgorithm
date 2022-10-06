N = int(input())
results = []
for i in range(N):#range로 안쓰고 값 정해둠
  A,B = map(int,input().split())
  results.append(A+B)#배열을 만들고 거기에 더해줘서 한꺼번에 출력
for result in results:
  print(result)
#   N = int(input())
# for i in range(0,5):
#     A,B = map(int,input().split())
#       print(f"{A+B}")