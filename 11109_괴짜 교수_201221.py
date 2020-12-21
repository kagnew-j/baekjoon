for _ in range(int(input())):
    d,n,s,p = map(int,input().split())
    curr = n*s
    para = d + n*p
    if curr > para:
        print("parallelize")
    elif curr < para:
        print("do not parallelize")
    else:
        print("does not matter")

# https://www.acmicpc.net/problem/11109