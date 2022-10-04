def solution():
    n, k = input().split()
    k = int(k)
    n = int(n)
    coins = []
    for i in range(int(n)):
        coins.append(int(input()))
    coins.sort(reverse=True)
    ans = 0
    for coin in coins:
        if k == 0:
            break
        if k//coin:
            repeat = k//coin
            k -= coin*repeat
            ans+= repeat
    return ans
print(solution())