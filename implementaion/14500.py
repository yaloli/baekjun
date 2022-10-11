from bdb import Breakpoint
def solution():
    # 시작 11:22 일시정지 12:00 다시시작 1:00 끝 2:00
    # 대칭, 회전한 테트로미노의 총 가짓수는 19가지이다. 500*500*19*4이니까 가능// 브루트포스로 구현해야하는 문제
    # 도형을 맵핑해보자

    tetrominos = {
        0: [(0,1),(0,2),(0,3),(0,0)],
        1: [(1,0),(2,0),(3,0),(0,0)],
        2: [(0,0),(0,1),(1,0),(1,1)],
        3: [(0,0),(1,0),(2,0),(2,1)],
        4: [(1,0),(1,1),(1,2),(0,2)],
        5: [(0,0),(0,1),(1,1),(2,1)],
        6: [(0,0),(0,1),(1,0),(0,2)],
        7: [(0,1),(1,1),(2,0),(2,1)],
        8: [(0,0),(0,1),(0,2),(1,2)],
        9: [(0,0),(1,0),(2,0),(0,1)],
        10: [(0,0),(1,0),(1,1),(1,2)],
        11: [(0,0),(1,0),(1,1),(2,1)],
        12: [(1,0),(1,1),(0,1),(0,2)],
        13: [(0,1),(1,0),(1,1),(2,0)],
        14: [(0,0),(0,1),(1,1),(1,2)],
        15: [(0,0),(0,1),(0,2),(1,1)],
        16: [(0,0),(1,0),(2,0),(1,1)],
        17: [(0,1),(1,0),(1,1),(1,2)],
        18: [(0,1),(1,0),(1,1),(2,1)]
        }
    N, M = map(int, input().split())
    jido = []

    for _ in range(N):
        jido.append(list(map(int, input().split())))
    max_hap = 0
    for i in range(N):
        for j in range(M):
            calc_dic = {}
            for n in range(i, N):
                for m in range(j, M):
                    calc_dic[(n-i, m-j)] = jido[n][m]
            for n in tetrominos:
                tertromino = tetrominos[n]
                hap = 0
                for jwapyo in tertromino:
                    if calc_dic.get(jwapyo, False):
                        hap+=calc_dic[jwapyo]
                    else:
                        hap = 0
                        break
                if hap>max_hap:
                    max_hap = hap
    answer = max_hap
    return answer

print(solution())