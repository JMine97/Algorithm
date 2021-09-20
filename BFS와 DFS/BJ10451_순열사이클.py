'''
배운점
- dfs는 들어오자마자 방문처리 해주자
'''

import sys

sys.setrecursionlimit(2000)
T = int(input())


def dfs(idx):  # 반복문과 유사
    visited[idx] = True #dfs 들어오자마자 방문처리
    number = num[idx]
    if not visited[number]:
        dfs(number)


for i in range(T):
    N = int(input())

    num = [0] + list(map(int, input().split()))
    end_idx = N + 1
    visited = [False] * end_idx

    cnt = 0
    for j in range(1, end_idx):
        if not visited[j]:
            cnt += 1
            dfs(j)
    print(cnt)
