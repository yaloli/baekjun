# 로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

# 로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 
# 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, 
# r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

# 로봇 청소기는 다음과 같이 작동한다.

def solution():
    # 시작 10:01 일시정지 10:25 복귀 10:50 끝 11:18
    N , M = map(int, input().split())
    r, c, d = map(int, input().split())
    jido = []
    for _ in range(N):
        jido.append(list(map(int, input().split())))

    global answer
    answer = 0

    def clean(r,c):
        global answer
        jido[r][c] = 2
        answer +=1

    def turn_left(d):
        d_dic = {0:3, 1:0, 2:1, 3:2}
        return d_dic[d]

    def check_direction(d, r, c):
        if d==0: # 북
            if jido[r-1][c]:
                return False
        elif d==1: # 동
            if jido[r][c+1]:
                return False
        elif d==2: # 남
            if jido[r+1][c]:
                return False
        elif d==3: # 서
            if jido[r][c-1]:
                return False
        return True

    def go_straight(d, r, c):
        if d==0: # 북
            r -= 1
        elif d==1: # 동
            c += 1
        elif d==2: # 남
            r +=1
        elif d==3: # 서
            c -= 1
        return (r,c)
    def go_backward(d, r, c):
        if d==0: # 북
            if jido[r+1][c]==1:
                return False
        elif d==1: # 동
            if jido[r][c-1]==1:
                return False
        elif d==2: # 남
            if jido[r-1][c]==1:
                return False
        elif d==3: # 서
            if jido[r][c+1]==1:
                return False
        if d==0: # 북
            r += 1
        elif d==1: # 동
            c -= 1
        elif d==2: # 남
            r -=1
        elif d==3: # 서
            c += 1
        return (r,c)
# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
#   2-1 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
#   2-2 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
#   2-3 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
#   2-4 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
    success = 1
    while True:
        if success:
            clean(r,c)
        for _ in range(4): 
            d = turn_left(d)
            success = 0
            if check_direction(d, r, c):
                r, c = go_straight(d, r, c)
                success=1
                break
        if not success:
            # 네 방향 모두 청소가 되어있거나 벽인경우
            if go_backward(d, r, c):
                r, c = go_backward(d, r, c)
            else:
                return answer

print(solution())