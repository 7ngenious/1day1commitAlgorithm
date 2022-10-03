A,B = map(int,input().split())
C = int(input())
H = int(A+(B+C)/60)
M = (B+C)%60
if H >= 24:
  H= H-24

print(H,M,sep=" ")