N = int(input())
score = list(map(int, input().split()))
max_num = max(score)
sum = 0
for i in score:
    i = i/max_num*100
    sum += i
print(sum / N)