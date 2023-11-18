# 행렬의 크기 N, M 입력 받기
N, M = map(int, input().split())

# 행렬 A 입력 받기
matrix_A = []
for _ in range(N):
    row_A = list(map(int, input().split()))
    matrix_A.append(row_A)

# 행렬 B 입력 받기
matrix_B = []
for _ in range(N):
    row_B = list(map(int, input().split()))
    matrix_B.append(row_B)

# 결과 행렬 초기화
result_matrix = [[0 for _ in range(M)] for _ in range(N)]

# 행렬 덧셈 수행
for i in range(N):
    for j in range(M):
        result_matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]

# 결과 출력
for row in result_matrix:
    print(*row)