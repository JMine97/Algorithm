from collections import deque
#양방향 데이터 처리 가능 자료구조

def bfs(graph, start, visited):
    # 시작 값으로 큐 초기화
    queue = deque([start])
    # 시작 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 방문하지 않은 인접 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 표현(0번 인덱스는 무시)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문한 정보를 표현
visited=[False]*9

bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6