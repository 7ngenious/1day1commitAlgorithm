N, M = map(int, input().split())
baskets = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    baskets[i - 1 : j] = [k] * (j - i + 1)
print(" ".join(map(str, baskets)))
