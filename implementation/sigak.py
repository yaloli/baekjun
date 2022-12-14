
def solution():
    # 시작 2:15 끝 2:22
    # 시간제한 2초, 메모리제한 128MB
    # 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오
    # 예를 들어 1을 입력했을 떄 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다 00시 00분 03초, 00시 13분 30초
    # 반면에 다음은 3이 하나라도 포함되어 있지 않으므로 세면 안되는 시각이다.
    # 00시 02분 55초, 01시 27분 45초
    # 첫째줄에 정수 N이 입력된다.
    N = int(input())
    H = 0
    M = 0
    S = 0
    answer = 0
    while not (H==N and M ==59 and S ==59):
        if '3' in str(H)+str(M)+str(S):
            answer +=1
        S+=1
        if S==60:
            S = 0
            M += 1
        if M == 60:
            H += 1
            M = 0
    return answer

print(solution())