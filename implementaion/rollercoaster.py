# 상근이는 우리나라에서 가장 유명한 놀이 공원을 운영하고 있다. 이 놀이 공원은 야외에 있고, 다양한 롤러코스터가 많이 있다.

# 어느 날 벤치에 앉아있던 상근이는 커다란 황금을 발견한 기분이 들었다. 자신의 눈 앞에 보이는 이 부지를 구매해서 롤러코스터를 만든다면, 
# 세상에서 가장 재미있는 롤러코스터를 만들 수 있다고 생각했다.

# 이 부지는 직사각형 모양이고, 상근이는 R행 C열의 표 모양으로 나누었다. 롤러코스터는 가장 왼쪽 위 칸에서 시작할 것이고,
# 가장 오른쪽 아래 칸에서 도착할 것이다. 롤러코스터는 현재 있는 칸과 위, 아래, 왼쪽, 오른쪽으로 인접한 칸으로 이동할 수 있다. 
# 각 칸은 한 번 방문할 수 있고, 방문하지 않은 칸이 있어도 된다.

# 각 칸에는 그 칸을 지나갈 때, 탑승자가 얻을 수 있는 기쁨을 나타낸 숫자가 적혀있다. 
# 롤러코스터를 탄 사람이 얻을 수 있는 기쁨은 지나간 칸의 기쁨의 합이다. 
# 가장 큰 기쁨을 주는 롤러코스터는 어떻게 움직여야 하는지를 구하는 프로그램을 작성하시오.

def solution():
    # 시작 2:52 끝 4:12
    R, C = map(int, input().split())
    jido = [list(map(int, input().split())) for _ in range(R)]
    answer = ''
    # 홀수일때
    if R % 2 == 1:
        for i in range(1, R+1):
            if i%2==1:
                answer+='R'*(C-1)
            else:
                answer+='L'*(C-1)
            if i == R:
                break
            answer+='D'
    elif C%2 == 1:
        for i in range(1, C+1):
            if i%2==1:
                answer+='D'*(R-1)
            else:
                answer+='U'*(R-1)
            if i == C:
                break
            answer+='R'
    if C%2==1 or R%2==1:
        return answer
    # 짝수일때 r와 c의 합의 홀수인 녀석들 중 하나를 골라서 버려야함.
    # 두 개 단위로 보아서 다음줄에 피해야할 녀석이 있다면 지그재그로 주파함.
    # 버릴거 정하기 
    minimum = 1000
    burilge = False
    for r in range(R):
        for c in range(C):
            if (r+c)%2==1:
                if minimum>jido[r][c]:
                    minimum = jido[r][c]
                    burilge = (r,c)
    if burilge:
        after_burim = 0
        for i in range(0, R, 2):
            # 버릴거의 R과 i의 차이가 2미만이 되면
            # 지그재그 주파법 : 버릴거의 C와 같은 위치에 지금이 있다면 무조건 오른쪽으로 가면 됨.
            if 0<=burilge[0]-i<2:
                bungala = ['D', 'U']
                k = 0
                for j in range(C-1):
                    if j == burilge[1]:
                        answer+='R'
                    else:
                        answer+=bungala[k%2]
                        answer+='R'
                        k+=1
                if bungala[k%2]=='D':
                    answer+='D'
                after_burim = 1
            else:
                if after_burim:
                    answer+='L'*(C-1)
                    answer+='D'
                    answer+='R'*(C-1)
                else:
                    answer+='R'*(C-1)
                    answer+='D'
                    answer+='L'*(C-1)
            if i+2 == R:
                break
            answer+='D'
    return answer

print(solution())
""""
6 6
100 100 100 100 100 99
100 100 100 100 100 100
100 100 100 100 100 100
100 100 100 100 100 100
100 100 100 100 100 100
100 100 100 100 100 100
"""