# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 
# 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
# 용량이 더 큰 보석이 가격이 더 낮은경우
# 4, 3 / 2, 5, 10 이고, 보석은 2, 40 / 2, 50 / 10, 40 / 5, 25 => 130
from heapq import heappop, heappush
from sys import stdin

def solution():
    # 시작 7:06 끝 8:41 다음에 다시 보기!!
    # 가방용량이 작은것부터 해서 그리디로 풀면 풀리지 않을까?
    ans = 0
    n, k = map(int, stdin.readline().split())
    germs = []
    bags = []
    for _ in range(n):
        M, V = map(int, stdin.readline().split())
        heappush(germs,[M, V])
    for _ in range(k):
        bags.append(int(stdin.readline()))
    
    bags.sort()
    hubo = []
    for bag in bags:
        while germs and germs[0][0]<=bag:
            heappush(hubo, -heappop(germs)[1])
        if hubo:
            ans-=heappop(hubo)
        elif not germs:
            break
    return ans

print(solution())