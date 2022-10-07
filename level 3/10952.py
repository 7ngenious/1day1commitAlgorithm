# A,B = map(int,input().split())
# while(A!=0 and B!=0):
#   print(A+B)
#   A,B = map(int,input().split())
while True:
  try:#실행할 코드
    a, b = map(int, input().split())
    print(a+b)
  except:#예외가 발생했을 때 처리하는 코드
    break