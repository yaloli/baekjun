# 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
# 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
# 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
# 두 수의 합은 99437이 되어서 최대가 될 것이다.

# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

def solution():
    # 시작 4:44 끝 5:39
    # 무조건 큰 자리수에 큰 수를 주면 됨
    # 길이 비교후 앞에서부터 알파벳에 숫자 부여
    # 갈아 엎어보자!! 5:32 각 자릿수를 더해서 딕셔너리에다가 저장 무슨말이냐면 ABCD 가 있으면 A에 1000 B에 100 C에 10 D에 1 추가, 모든 문자에 대해
    # 반례 : ABC BBA BCC 같은 경우엔 A에 9가 아니라 B에 9가 들어가야 최대이다. 따라서 숫자 부여할때 해당 자리에 가장 많이 있는 알파벳에 큰 수를 부여해야한다.
    #       897 998 977  2872
    # ABCDEFG
    # GFEDCBH
    dic = {}
    ans = 0
    N = int(input())
    strings_arr = []
    for _ in range(N):
        strings_arr.append(input())
    max_leng = max([len(x) for x in strings_arr])
    strings = [x.zfill(max_leng) for x in strings_arr]
    numbers = [9,8,7,6,5,4,3,2,1,0]
    now_ind = 0
    alphabets = {}
    for i in range(max_leng):
        for string in strings:
            if string[i]!= '0':
                alphabets[string[i]]= alphabets.get(string[i], 0)+10**(max_leng-i-1)
    alphabets = dict(sorted(alphabets.items(), key=lambda x:x[1], reverse=True))
    for eng in alphabets:
        if eng in dic:
            pass
        else:
            dic[eng]= numbers[now_ind]
            now_ind+=1

    for string in strings_arr:
        to_num=''
        for c in string:
            to_num+=str(dic[c])
        ans+=int(to_num)
    return ans

print(solution())