'''
bfs 풀이
'''

from collections import deque

N, M = map(int, input().split())
end_r = N - 1
end_c = M - 1
CAN_GO = '1'
CAN_NOT_GO = '0'
maze = []
for i in range(N):
    maze.append(list(input()))

def bfs():
    q = deque()
    q.append([0, 0, 1])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    while (q):
        r, c, cnt = q.popleft()
        for dr, dc in [0, 1], [0, -1], [1, 0], [-1, 0]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == CAN_GO and not visited[nr][nc]:
                if nr == N - 1 and nc == M - 1:
                    return cnt + 1
                q.append([nr, nc, cnt + 1])
                visited[nr][nc] = True


print(bfs())
