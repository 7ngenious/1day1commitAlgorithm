arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
#set함수는 간단하게 말하면, 중복을 제거하기 위한 필터역할
#set 생성자에 iterable한 객체를 넣으면 변환하여 set을 만들어 준다
# 집합은 순서가 없고, 집합안에서는 unique한 값을 가지는 자료형
print(len(arr))
# for num in num_list:
#     if num not in result_list:
# 중복확인 메커니즘