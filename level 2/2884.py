A,B = map(int,input().split())
if B <45 :
  if A == 0: 
    A =A+24
  A =A-1
  B=B+15
else: B= B-45
print(A,B,sep=" ")
