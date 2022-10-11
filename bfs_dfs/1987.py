
def solution():
    # 시작 20:17 끝 20:45
    R, C = map(int, input().split())
    jido = []
    for _ in range(R):
        str1 = input()
        jido.append([str1[i] for i in range(C)])
    # DFS로 풀되 현재의 상태를 리스트에 저장해놓고 다음 탐색할게 now에 있으면 넣지 말자
    # 재귀함수로 푸는게 편할듯 넘길 값 : 현재 위치 now, 탐색완료한 알파벳들, 
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    global max_searched 
    global cached
    cached ={}
    max_searched = 0
    def dfs(now, searched, jido):
        global max_searched
        to_search = []
        searched.append(jido[now[0]][now[1]])
        if len(searched)>max_searched:
            max_searched = len(searched)
        for i in range(4):
            r = now[0]+dr[i]
            c = now[1]+dc[i]
            if R>r>=0 and C>c>=0:
                if jido[r][c] not in searched:
                    to_search.append((r,c))
        for jwapyo in to_search:
            key = {'jwapyo':jwapyo, 'searched':searched+[]}
            if cached.get(str(key), False):
                pass
            else:
                dfs(jwapyo, searched+[], jido)
                cached[str(key)] = True
    dfs((0,0), [], jido)
    answer = max_searched
    return answer

print(solution())