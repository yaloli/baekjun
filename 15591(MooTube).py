# 시작  9:01 끝 10:08
#  다익스트라 알고리즘인듯
# 아님 dfs임, 이유: 길이 유일함

# dfs로 풀면 메모리초과, bfs로 풀어야 하는 문제, 
# bfs도 메모리 낭비없이 해시사용해서 풀어야 시간 초과 피할 수 있음
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