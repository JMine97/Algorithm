'''
크기가 N+1인 배열을 이용하고 싶다면
추가로 end_index 변수 만들어주기
'''

from collections import deque

N, M, V = map(int, input().split())
end_index = N + 1
arr = [[] for _ in range(end_index)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    arr[b].append(a)
visited = [False] * end_index

for i in range(end_index):
    arr[i].sort()


def dfs(start):
    print(start, end=" ")
    visited[start] = True
    for node in arr[start]:
        if not visited[node]:
            dfs(node)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = False
    while q:
        start = q.popleft()
        print(start, end=" ")
        for node in arr[start]:
            if visited[node]:
                visited[node] = False
                q.append(node)


dfs(V)
print()
bfs(V)
