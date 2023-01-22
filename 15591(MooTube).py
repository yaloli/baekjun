# 시작  9:01
#  다익스트라 알고리즘인듯
# 아님 dfs임, 이유: 길이 유일함
from collections import deque

def solution():
    def bfs(start, k, result, searched):
        queue = deque([start])
        while queue:
            now = queue.popleft()
            searchable = [x for x in neighbor.get(now, []) if x not in searched]
            for near in searchable:
                if jido.get((now,near), jido.get((near,now),0))>=k:
                    queue.append(near)
                    result.append(near)
            searched.add(now)

    N, Q = map(int, input().split())
    jido = {}
    neighbor = {}
    
    for _ in range(N-1):
        p, q, r = map(int, input().split())
        jido[(p,q)]=r
        neighbor[q] = neighbor.get(q, []) + [p]
        neighbor[p] = neighbor.get(p, []) + [q]

    for _ in range(Q):
        result = []
        searched = set()
        k, v = map(int, input().split())
        bfs(v, k, result, searched)
        print(len(result))

solution()