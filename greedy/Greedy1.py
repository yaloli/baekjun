def solution():
    n, m, k = input().split()
    data = input().split()
    data = [int(x) for x in data]
    data.sort(reverse=True)
    ans = 0
    for i in range(int(m)):
        if (i+1) % (int(k)+1):
            ans+=data[0]
            print(data[0])
        else:
            ans+=data[1]
            print(data[1])

    return ans

print(solution())