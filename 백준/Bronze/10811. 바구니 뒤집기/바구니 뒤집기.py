N,M = map(int,input().split())
arr = [x+1 for x in range(N)]
for _ in range(M):
    i,j = map(int,input().split())
    tmp = arr[i-1:j]
    tmp.reverse()
    arr[i-1:j] = tmp     
for i in arr:
    print(i,end=" ")    