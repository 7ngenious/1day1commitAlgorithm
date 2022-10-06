# N = int(input())
# for i in [1,2,3,4,5,6,7,8,9]: //range함수 활용하기
#   print(N,"*",i,'=',N*i) // 변수 print 안에 넣는 법 익히기
num = int(input())

for i in range(1, 10):
    print(f"{num} * {i} = {num*i}")
# print("{} * {} = {}".format(n, i, n*i))//이것도 있다