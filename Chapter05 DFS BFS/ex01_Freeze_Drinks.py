# - 문제 
# N * M 크기의 얼음 틀이 있음
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
# 구멍이 뚫려 있는 부분끼리 상 하 좌 우 붙어 있는 경우, 서로 연결되어 있는 것으로 간주
# 얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림 개수를 구해라

# - 핵심 
# 묶음을 찾는 프로그램을 만들기

# 1. 특정한 지점의 주변 상 하 좌 우 를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# 2. 방문한 지점에서 다시 상 하 좌 우 를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다
# 3. 1~2 과정을 모든 노드에 반복하면서 방문하지 않은 지점의 수를 센다

# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기 
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문 
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    # 현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우 의 위치도 모두 재귀적으로 호출 
        dfs(x - 1, y) # 상
        dfs(x , y - 1)  # 좌
        dfs(x + 1, y)   # 하
        dfs(x, y + 1)   # 우
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기 
result = 0
for i in range(n): 
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
    