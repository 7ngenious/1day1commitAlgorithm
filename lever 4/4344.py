# N = int(input())
# for i in range(N):
#   Slist = input().split()
#   number = int(Slist[0])
#   setlist = list(map(int, [Slist[i+1] for i in range(number)]))
#   avg=sum(setlist) / number
#   a=0
#   for j in setlist:
#     if j> avg: a= a+1
#   print(str(f"{(a*100)/number:.3f}")+'%')
num = int(input())

for _ in range(num):#단순 반복을 위한 공백
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')