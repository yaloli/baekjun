def solution():
    N = int(input())
    for i in range(int(N//5), -1, -1):
        leftover = N - 5*i
        if leftover%3==0:
            return i+int(leftover/3)
    return -1
print(solution())