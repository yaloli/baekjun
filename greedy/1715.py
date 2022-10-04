# 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 
# 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

# 매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 
# 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다.
# 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

from heapq import heappush, heappop
def solution():
    # 한 번 연산할때마다 연산결과 append하고 정렬하기 => 시간초과뜨면 직접 알맞은 위치에 넣기까지 구현
    # heapq를 이용해서 항상 sort 된 상태로 유지
    N = int(input())
    num = []
    ans = 0
    for _ in range(N):
        num.append(int(input()))
    num.sort()
    while len(num)>1:
        new_deck = heappop(num) + heappop(num)
        ans += new_deck
        heappush(num, new_deck)

    return ans

print(solution())
# print(merge([1,2,3,4,5,6],[4]))