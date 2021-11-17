# 1260
from collections import deque # bfs

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
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
computers = int(sys.stdin.readline())
connections = int(sys.stdin.readline())
graph = [[] for _ in range(computers + 1)]

for i in range(connections):
    a, b = map(int, sys.stdin.readline().split())
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

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline())))

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
T = int(sys.stdin.readline())

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
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]

    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1

    print(cnt)

# 2178
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline())))

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

m, n = map(int, sys.stdin.readline().split())
graph = []
que = deque([])
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
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

n, k = map(int, sys.stdin.readline().split())
max = 100000
dist = [0] * (max + 1)

bfs()

# 7569
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
graph = []
que = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split()))) # sys.stdin.readline() 쓰면 런타임에러
        for k in range(m):
            if tmp[j][k] == 1:
                que.append([i,j,k])
    graph.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while que:
    x,y,z = que.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0:
            que.append([nx, ny, nz])
            graph[nx][ny][nz] = graph[x][y][z] + 1

answer = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer - 1)

# 2206
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    que = deque()
    que.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1 # 벽을 한번 부술 수 있는 상태에서 시작

    while que:
        x, y, z = que.popleft()
        if x==n-1 and y==m-1:
            return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 1: # 벽을 만났고 벽을 한번 부술 수 있을 때
                    visit[nx][ny][0] = visit[x][y][z] + 1
                    que.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visit[nx][ny][z] == 0: # 벽이 없고 방문한 적이 없는 경우
                    visit[nx][ny][z] == visit[x][y][z] + 1
                    que.append([nx, ny, z])
    return -1

n,m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

print(bfs())

# 7562
from collections import deque
import sys

T = int(sys.stdin.readline())
for i in range(T):
    l = int(sys.stdin.readline())
    a,b = map(int, sys.stdin.readline().split())
    c,d = map(int, sys.stdin.readline().split())
    graph = [[0] * l for i in range(l)]

    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    def bfs(a, b, c, d):
        que = deque()
        que.append([a, b])
        graph[a][b] = 1
        while que:
            x, y = que.popleft()
            if x == c and y == d:
                print(graph[c][d]-1)
                return
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                    que.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1

    bfs(a, b, c, d)