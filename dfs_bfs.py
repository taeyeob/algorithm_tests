# 1260
from collections import deque # bfs

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


visited = [False] * (n + 1)

def Dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            Dfs(graph, i, visited)

def Bfs(graph, v, visited):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

Dfs(graph, v, visited)
print()
Bfs(graph, v, visited)

# 2606
computers = int(input())
connections = int(input())
graph = [[] for _ in range(computers + 1)]

for i in range(connections):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (computers + 1)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

print(visited.count(True) - 1)

# 2667
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

grp = []
cnt = 0
dx = [-1, 1, 0, 0] # 방향
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if graph[x][y] == 1: # 세대가 있는 경우
        cnt += 1
        graph[x][y] = 0 # 중복되지 않기 위해 0으로 바꿔줌
        for i in range(len(dx)):
            dfs(x + dx[i], y + dy[i]) # 이동
        return True

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True: # 단지가 연결되는 경우
            grp.append(cnt)
            cnt = 0

print(len(grp))
grp.sort() # 오름차순으로 출력
for i in grp:
    print(i)

# 1012
from collections import deque
T = int(input())

dx = [0, 0, 1, -1] # 입력방향, 좌표값인 (a, b)는 리스트에서 list[b][a]이기 때문
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    que = deque()
    que.append((a, b))
    graph[a][b] = 0

    while que:
        x,y = que.popleft()
        for i in range(4): # 움직이는 방향의 수(상하좌우)
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # visited
                que.append((nx, ny))
    return

for i in range(T):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1

    print(cnt)

# 2178
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    que = deque()
    que.append((a, b))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 길을 잘못 들었을 때 다시 돌아와도 원래의 상태에서 시작될 수 있음. cnt += 1 로 하면 17이 되지만 이렇게 하면 최소경로 찾기 가능
                que.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))

# 7576
from collections import deque

m, n = map(int, input().split())
graph = []
que = deque([])
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append([nx, ny])

bfs()
answer = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answer = max(answer,max(i))
print(answer-1)

# 1697
from collections import deque

def bfs():
    que = deque()
    que.append(n)

    while que:
        x = que.popleft()
        if x == k:
            print(dist[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= max and not dist[j]:
                dist[j] = dist[x] + 1
                que.append(j)

n, k = map(int, input().split())
max = 100000
dist = [0] * (max + 1)

bfs()