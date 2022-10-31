# 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, 
# r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

# 이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

# 예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.
import itertools
def solution():
    # 시작 : 9:38 끝 10:21
    # 구현문제 => 각 치킨집 별로 각 집에 대한 치킨거리를 계산한다. 좌표:[거리1, 거리2, 거리3, 거리4]
    # M갯수만큼 골라서 계산된 치킨거리를 모두 합하여 최소값을 구한다. 고른 아이들 중에 min 들의 sum
    N, M = map(int, input().split())
    jido = [list(map(int, input().split())) for _ in range(N)]
    chickens = []
    jibs = []
    chi_jib_dis = {}
    for i in range(N):
        for j in range(N):
            if jido[i][j]==2:
                chickens.append((i,j))
            elif jido[i][j]==1:
                jibs.append((i,j))
    for index, chicken in enumerate(chickens):
        for jib in jibs:
            chi_jib_dis[index]=chi_jib_dis.get(index, [])+[abs(chicken[0]-jib[0])+abs(chicken[1]-jib[1])]
    possible = list(itertools.combinations(list(chi_jib_dis.keys()), M))
    min_sub = 10**10
    for case in possible:
        sb = 0
        for i in range(len(jibs)):
            sb+=min([chi_jib_dis[chi][i] for chi in case])
        if sb<min_sub:
            min_sub = sb
    answer = min_sub
    return answer

print(solution())