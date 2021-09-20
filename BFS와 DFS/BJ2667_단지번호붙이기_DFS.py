'''
배운점
- 방문한 지점을 '0'으로 바꿔주면 visited 배열을 쓰지 않아도 된다
'''

N = int(input())
apart = []
for _ in range(N):
    apart.append(list(input()))
visited = [[False] * N for _ in range(N)]
ret = []


def dfs(r, c):
    if 0 <= r < N and 0 <= c < N and apart[r][c] == '1' and not visited[r][c]:
        global cnt
        cnt += 1
        visited[r][c] = True
        dfs(r + 1, c)  # 사방탐색
        dfs(r - 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)


for i in range(N):
    for j in range(N):
        if apart[i][j] == '1' and not visited[i][j]:
            cnt=0
            dfs(i, j)
            ret.append(cnt)

print(len(ret))
ret.sort()
for r in ret:
    print(r)
