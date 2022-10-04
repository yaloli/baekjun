# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

def solution():
    # -를 기준으로 쪼개면 무조건 최소값이 나오지 않을까
    ans = 0
    f = input().split('-')
    for ind, formular in enumerate(f):
        sik = formular.split('+')
        sub_res = 0
        for nums in sik:
            sub_res+=int(nums)
        if ind:
            ans-=sub_res
        else:
            ans+=sub_res

    return ans

print(solution())