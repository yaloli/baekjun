# 옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

# S의 최솟값을 출력하는 프로그램을 작성하시오.


def solution():
    # 이것도 그리디로 가능한가? 제한시간 2초면 nlogn 이라는건데 결국 정렬한다음에 걍 곱해야 가능한 수준..

    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = 0
    A.sort()
    B.sort(reverse=True)
    for ind, a in enumerate(A):
        ans+=a*B[ind]
    return ans

print(solution())