from collections import deque
def solution():
    # 시작 20:10  끝 20 :16
    # bfs문제네요. 탐색끝날때까지 돌리고 총 탐색된 노드 수 세면 되는 문제
    V = 1
    N = int(input())
    M = int(input())
    link = {}
    answer = -1
    searched = {}
    for _ in range(M):
        V1, V2 = map(int, input().split())
        searched[V1]=0
        searched[V2]=0
        link[V1]=link.get(V1, [])+[V2]
        link[V2]=link.get(V2, [])+[V1]

    for key in link:
        link[key] = list(set(link[key]))
        link[key].sort()

    queue = deque([V])
    # bfs는 큐로 구현한다. 필요한 연산 : append, popleft()
    while queue:
        now = queue.popleft()
        if searched[now]:
            pass
        else:
            answer += 1
            searched[now]=1
            if link.get(now, False):
                queue+=[x for x in link[now]]
    return answer

print(solution())