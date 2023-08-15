# 미로는 BFS
from collections import deque
n, m = map(int, input().split())
graph = []
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 큐 생성
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 상하좌우 중 갈 수 있는 곳이면 +1 해줌
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0,0))