def d(n) :
    result = n
    for _ in range(len(str(n))):
      result +=n%10
      if n >=10:
          n//=10
    return result
list=list(range(10000))
for i in range(1,10000):
    while d(i)<10000:
        i=d(i)
        list[i]=0

for j in range(1,10000):
  if list[j]!=0:
    print(j)

# def d(n) :
#     result = n
#     for i in range(len(str(n))):
        
#         result +=n%10
#         if n >=10:
#             n//=10
#     return result


# #1부터 10000보다 작은 수만큼의 true를 값으로 하는 리스트 만든 후
# #d(n)에 1부터 9999넣은다음에 d(n)값이 100000보다 작을떄 까지 계속 넣고 나올떄마다

# list=list(range(10000))# 0도 있지만 무시하고 1부터 9999개까지의 항목을 만들기위함

# for k in range(1,10000):
#     #1부터 9999까지
#     while d(k)<10000 and k!=d(k):
#         k=d(k)
#         list[k]=0
# for j in range(1,10000):#여기서 0은 어차피 안씀으로
#     if list[j]!=0:
#         print(j)