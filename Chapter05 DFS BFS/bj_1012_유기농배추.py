# 덩어리 구하기 
# DFS 로 풀기
def dfs(x, y):
    # 범위 내 인데, 미방문 했으면 방문으로 바꾸고 상하좌우 확인 -> 상하좌우가 아닌 인접한 경우임
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i] 
        if (0 <= nx < n) and (0 <= ny < m): 
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
                return True
    return False
t = int(input())
for i in range(t):
    n, m, k = map(int,input().split())
    # 그래프 생성
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    result = 0
    for i in range(n):
        for j in range(len(graph[i])):
            if dfs(i, j) == True:
                result += 1
    print(result)