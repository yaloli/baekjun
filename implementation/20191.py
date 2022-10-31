# 문자열 A가 문자열 B의 줄임말이라는 것은 B의 순서를 바꾸지 않고 0 또는 그 이상 개수의 문자를 지워 A를 만들 수 있다는 뜻이다. 
# 정의에 의해서 B는 자기 자신의 줄임말임에 유의하라. 예를 들어, ac, ab, aa, aabc는 aabc의 줄임말이고, d, aaa, ba는 aabc의 줄임말이 아니다.

# 영문 알파벳 소문자로만 이루어진 두 문자열 S와 T가 주어진다. T를 자연수 n번 반복해서 이어쓴 문자열을 T n이라고 하자. S가 T n의 줄임말이 되는 최소의 n을 구하라.

# 예를 들어, T = ac, S = caa라고 하면, T1 = T = ac, T2 = acac, T3 = acacac이고 n = 3일 때 처음으로 S가 Tn의 줄임말이 된다.

def solution():
    # 시작 15:15 끝 15:30분에 42점  16:08 에 68점
    S = input()
    T = input()
    alphabet_S = [x for x in S]
    alphabet_T = {}
    for i, w in enumerate(T):
        alphabet_T[w] = alphabet_T.get(w, [])+[i]
    if set(alphabet_S)-set(alphabet_T):
        return -1

    answer=0
    S_ind = 0
    T_ind = 0
    # print(alphabet_T)
    cache = {}
    # 시간을 어디서 잡아먹을까?
    while S_ind<len(S):
        if S[S_ind:S_ind+len(T)-T_ind]==T[T_ind:]!='':
            print("S:",S[S_ind:S_ind+len(T)-T_ind],S_ind,S_ind+len(T)-T_ind)
            print("T:",T[T_ind:], T_ind)
            answer+=1
            S_ind+=(len(T)-T_ind)
            T_ind = 0
            continue
        w = alphabet_S[S_ind]
        hubo = [x for x in alphabet_T[w] if x>=T_ind]
        if hubo:
            T_ind = min(hubo)+1
            S_ind+=1
        else:
            print(S_ind)
            answer+=1
            T_ind = 0
            answer+=1
    return answer

print(solution())