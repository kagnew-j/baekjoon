for i in range(int(input())):
    a,b=input().split()
    b=list(b)
    del b[int(a)-1]
    print("".join(b))

# https://www.acmicpc.net/problem/2711