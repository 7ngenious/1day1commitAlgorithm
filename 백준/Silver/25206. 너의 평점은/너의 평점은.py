grade = ["F","D0","D+","C0","C+","B0","B+","A0","A+"]
sum_N = 0
sum_k = 0
for _ in range(20):
    str, N, k = input().split()
    N = float(N)
    if k == "P":
        continue
    sum_N += N
    for i in grade:
        if k == i:
            idx = grade.index(i)
            break
    if idx != 0:
        sum_k += N * ((idx+1)*0.5)
print(sum_k/sum_N)