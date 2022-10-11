
def solution():
    # 시작 2:23 끝
    # 체스판 안의 한 점에서 나이트가 갈 수 있는 경우의 수 구하기
    e_to_n = {'a':1, 'b':2, 'c':3, 'd':4, 'e':4, 'f':3, 'g':2, 'h':1}
    n_to_n = {'1':1, '2':2, '3':3, '4':4, '5':4, '6':3, '7':2, '8':1}
    now = input()
    case = [[0,0,0,0,0],[0, 2,3,4,4],[0, 3,4,6,6],[0, 4,6,8,8],[0, 4,6,8,8]]

    answer = case[e_to_n[now[0]]][n_to_n[now[1]]]
    return answer

print(solution())