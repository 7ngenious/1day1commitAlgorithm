N, M = map(int, input().split())
baskets = [x+1 for x in range(N)] 
for _ in range(M):
    i, j= map(int, input().split())
    tmp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = tmp
print(" ".join(map(str,baskets)))