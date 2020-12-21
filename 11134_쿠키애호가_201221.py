for _ in range(int(input())):
    a,b=map(int,input().split())
    if a % b == 0 :
        print(a//b)
    else:
        print(a//b+1)
        
# https://www.acmicpc.net/problem/11134