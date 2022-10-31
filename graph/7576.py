from collections import deque
def solution():
    # 시작 17:22 끝 6:23
    # M 이 가로 N이 세로
    M, N = map(int, input().split())
    jido = [list(map(int, input().split())) for _ in range(N)]
    starting_point = []
    total_zero = []
    for i in range(N):
        for j in range(M):
            if jido[i][j]==1:
                starting_point.append((i,j))
            elif jido[i][j]==0:
                total_zero.append((i,j))
    if not total_zero:
        return 0

    distance = {}
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for wichi in starting_point:
        distance[wichi] = 0
        searched = {wichi:0}
    queue = deque(starting_point)
    while queue:
        now = queue.popleft()
        # print(now)
        for i in range(4):
            newi = now[0]+dx[i]
            newj = now[1]+dy[i]
            if 0<=newi<N and 0<=newj<M:
                if jido[newi][newj]==0 and (newi, newj) not in searched:
                    before = distance.get((newi,newj), 1000000)
                    after = distance[now]+1
                    if before<after:
                        pass
                    else:
                        queue.append((newi,newj))
                        searched[(newi,newj)] = 0
                        distance[(newi, newj)] = after
                    # print(newi, newj, distance[now])

    if len(total_zero)+len(starting_point)!= len(distance):
        return -1
    answer = max(list(distance.values()))
    return answer

print(solution())