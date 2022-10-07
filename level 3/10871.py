N ,X = map(int,input().split())
nums = map(int, input().split())
A = []
for n in nums:
  if(n<X):
    A.append(str(n))
#append():array.append(x) 형태로 사용
#()안에 값을 입력하면 새로운 요소를 array맨 끝에 객체로 추가
print(' '.join(A))
#".join(리스트):['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환
#'구분자'.join(리스트):'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로
#''.join(리스트)는 '구분자'.join(리스트)에서 '구분자'가 그냥 공백인 것과 같다

#그 밖에 extend(iterable):입력한 iterable 자료형의 항목 각각을 array의 끝에 하나씩 추가
#iterable 자료형:반복 가능한 자료형 List, Tuple, Dictionary, Set
#insert(i,x): array의 원하는 위치 i 앞에 추가할 값 x를 삽입 append에 위치만 추가된 형태

N ,X = map(int,input().split())
A = list(map(int,input().split()))
for i in A:
  if X > i:
    print(i, end='')
#end에 빈 문자열을 지정함녀 다음 번 출력으 바로 뒤에 오게 됨