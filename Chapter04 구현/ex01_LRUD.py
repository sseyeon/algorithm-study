# - 문제 
# 여행가는 N x N 크기의 정사각형 공간에 서 있다
# 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)
# 여행가는 상(U), 하(D), 좌(L), 우(R)로 움직일 수 있다
# 여행가의 최종 도착 좌표를 출력하시오

# - 입력 예시 
# 5
# R R R U D D 

# - 출력 예시
# 3 4

# 내 답변
n = int(input())
arr = list(map(str, input().split()))
x, y = 1, 1
for i in arr:
    if i == 'U':
        x -= 1
    elif i == 'D':
        x += 1
    elif i == 'L':
        y -= 1
    elif i == 'R':
        y += 1
    
    if x == 0 : x = 1
    if x > n : x = n
    if y == 0 : y = 1
    if y > n : y = n
print(x, y)

# ----------
# 더 나은 답변
# N을 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 확인 
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = x + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)