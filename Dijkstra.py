'''
graph의 역할 : 노드들이 몇의 가중치로 연결돼있는지 확인
distance의 역할 : 시작노드 (고정)-> 도착노드(인덱스값)까지의 최단 거리 담음
'''

import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 노드 b와 c의 가중치로 연결


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 거리, 노드
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:  # 이 간선은 볼 필요가 없다
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost


dijkstra(start)
print(distance)
