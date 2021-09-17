'''
dfs 풀이
'''

import sys

sys.setrecursionlimit(2000)
T = int(input())

for i in range(T):
    N = int(input())

    num = [0] + list(map(int, input().split()))
    end_idx = N + 1
    visited = [False] * end_idx


    def dfs(idx, start_value):
        if visited[idx]:
            return

        if start_value == num[idx]:
            global cnt
            cnt += 1
            return

        if not visited[idx]:
            visited[idx] = True
            dfs(num[idx], start_value)


    cnt = 0
    for i in range(1, end_idx):
        dfs(i, i)
    print(cnt)
