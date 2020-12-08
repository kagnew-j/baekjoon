for _ in range(int(input())):
    n,k=map(int,input().split())
    li = list(map(int,input().split()))
    cnt = 0
    for ele in li:
        cnt += ele//k
    print(cnt)

# https://www.acmicpc.net/problem/9550