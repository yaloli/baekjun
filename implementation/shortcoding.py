# 각 문자열의 길이가 가중치가 되고, 미니멈 스팬 트리를 찾아야 한다.
# 한바퀴 쭉 돌면서 == 으로 연결된 애들의 트리를 그린 다음, 
# ==이면 가장 작은걸로 치환 
# != 이여도 ==에서 그린 트리에서 가장 작은걸로 치환
# 시작 4:30
import sys
def solution():
    conditions = sys.stdin.readline().rstrip().split('&&')
    if len(conditions)==1:
        return conditions[0]
    answer = []
    vertex = {}
    ganso_vertex = {}

    for condition in conditions:
        if '==' in condition:
            hangs = condition.split('==')
            vertex[hangs[0]] = vertex.get(hangs[0],[])+[hangs[1]]
            vertex[hangs[1]] = vertex.get(hangs[1],[])+[hangs[0]]
        elif '!=' in condition:
            hangs = condition.split('!=')
            vertex[hangs[0]] = vertex.get(hangs[0],[])
            vertex[hangs[1]] = vertex.get(hangs[1],[])
    vertex_topdown = sorted(vertex.keys(), key = lambda x:len(x), reverse=True)

    for v in vertex_topdown:
        new_add = vertex.get(v, [])
        if new_add:
            new_add2 = []
            while True:
                for v2 in new_add:
                    new_add2 += [x for x in vertex[v2] if x not in vertex[v]+[v]]
                if not new_add2:
                    break
                vertex[v] += new_add2
                new_add = new_add2+[]
                new_add2 = []
            if vertex[v]:
                newhang = vertex_topdown[max([vertex_topdown.index(x) for x in vertex[v]])]
                # newhang = sorted(vertex[v], key = lambda x:len(x))[0]
                if v in vertex[newhang]:
                    vertex[newhang].remove(v)
                answer.append(f'{v}=={newhang}')
                ganso_vertex[v] = [newhang]
                ganso_vertex[newhang] = ganso_vertex.get(newhang, [])+[v]

    for condition in conditions:
        if '!=' in condition:
            hangs = condition.split('!=')
            vertex[hangs[0]] = vertex.get(hangs[0],[])
            vertex[hangs[1]] = vertex.get(hangs[1],[])
            if ganso_vertex.get(hangs[0], False):
                if len(hangs[0])>len(ganso_vertex[hangs[0]][-1]):
                    hangs[0] = ganso_vertex[hangs[0]][-1]
            if ganso_vertex.get(hangs[1], False):
                if len(hangs[1])>len(ganso_vertex[hangs[1]][-1]):
                    hangs[1] = ganso_vertex[hangs[1]][-1]
            answer.append(f"{hangs[0]}!={hangs[1]}")
    return "&&".join(answer)

print(solution())