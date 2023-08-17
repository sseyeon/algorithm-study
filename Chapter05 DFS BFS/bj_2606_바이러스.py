# DFS로 풀기 
n = int(input())    # 노드의 개수
v = int(input())    # 간선의 개수
# 그래프 초기화
graph = [[] for i in range(n+1)]
visited = [0] * (n + 1)
# 그래프 연결 
for i in range(v):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    # 범위 내에 방문하지 않았다면, 방문으로 바꾸고 연결 노드 확인 후 dfs 재수행
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)
dfs(1)

print(sum(visited) - 1)