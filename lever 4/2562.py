# max=0
# maxi = 0
# for i in range(1,10):
#   N=int(input())
#   if(N>=max):
#     max=N
#     maxi=i
# print(max)
# print(maxi)
l=[]
for i in range(9):
  l.append(input())
sort = list(map(int,l))
print(max(sort))
print(sort.index(max(sort))+1)