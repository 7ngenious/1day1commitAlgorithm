A,B,C = map(int,input().split())
if A == B ==C : 
  R = A * 1000 +10000
elif A ==B or B == C :
  R = B * 100 +1000
elif C==A:
  R = A * 100 +1000
else:
  if A> B: 
    if A>C:
      R = 100*A
    else:
      R= 100*C
  elif B > A:
    if B>C:
      R=100*B
    else:
      R=100*C
print(R)