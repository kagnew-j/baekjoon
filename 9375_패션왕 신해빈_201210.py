for _ in range(int(input())):
    n = int(input())
    di = dict()
    for i in range(n):
        a,b = input().split()
        di[b] = di.get(b,0) + 1
    ans = 1
    for ele in di.values():
        ans *= (ele+1)
    print(ans-1)

# https://www.acmicpc.net/problem/9375