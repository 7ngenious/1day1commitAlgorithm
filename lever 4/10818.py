# N = int(input())
# A = list(map(int,input().split()))
# max = 0
# min = A[0]
# for a in A:
#   if a >= max:
#     max=a
#   if a <= min:
#     min=a
# print(min,max)
N = int(input())
A = list(map(int,input().split()))
print(min(A),max(A))