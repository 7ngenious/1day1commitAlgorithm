A = int(input())
sum = int(A/10 + A%10)
sum2= int((A%10)*10 + sum%10)
cnt=1
while True:
  if(A==sum2):
    break
  sum = int(sum2/10 + sum2%10)
  sum2= int((sum2%10)*10 + sum%10)
  cnt +=1
print(cnt)