#dfs 재귀적 호출
def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v]=True
  print(v,end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

# 각 노드가 연결된 정보를 표현(0번 인덱스는 무시)
graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
# 각 노드가 방문한 정보를 표현
visited=[False]*9

#그래프, 현재노드, 방문기록
dfs(graph, 1, visited)