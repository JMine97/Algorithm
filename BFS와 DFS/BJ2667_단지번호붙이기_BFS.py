from collections import deque

N = int(input())
apart = []
for _ in range(N):
    apart.append(list(input()))
visited = [[False] * N for _ in range(N)]
ret = []


def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = True
    cnt = 1

    while q:
        r, c = q.popleft()
        for dr, dc in [-1, 0], [0, -1], [1, 0], [0, 1]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and apart[nr][nc] == '1' and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append([nr, nc])
                cnt += 1
    ret.append(cnt)


for i in range(N):
    for j in range(N):
        if apart[i][j] == '1' and not visited[i][j]:
            bfs(i, j)

print(len(ret))
ret.sort()
for r in ret:
    print(r)
