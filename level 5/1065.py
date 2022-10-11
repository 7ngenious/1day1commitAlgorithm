def self(n):
  cnt = 0
  if(n>=100):
    cnt = 99
    for i in range(100,n+1):
      n = list(map(int, str(i)))
      if n[0] - n[1] == n[1] - n[2]:
        cnt += 1
  else:
    cnt = n
  return cnt
n = int(input())
print(self(n))