# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
from collections import deque
def solution():
    # 시작 19:26 끝 20:09
    N, M, V = map(int, input().split())
    link = {}
    answer = ['','']
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
    searched2 = searched.copy()
    queue = deque([V])
    # bfs는 큐로 구현한다. 필요한 연산 : append, popleft()
    while queue:
        now = queue.popleft()
        if searched[now]:
            pass
        else:
            answer[1]+=str(now)+ " "
            searched[now]=1
            if link.get(now, False):
                queue+=[x for x in link[now]]
    # dfs 는 스택으로 구현한다. 필요한 연산 : append, pop()
    stack = deque([V])
    while stack:
        now = stack.pop()
        if searched2[now]:
            pass
        else:
            answer[0]+=str(now)+ " "
            searched2[now]=1
            if link.get(now, False):
                link[now].reverse()
                stack+=[x for x in link[now]]
    answer = [x[:-1] for x in answer]
    return "\n".join(answer)

print(solution())