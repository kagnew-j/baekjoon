for _ in range(int(input())):
    price = int(input())
    n = int(input())
    if n == 0:
        print(price)
    else:
        for i in range(n):
            a,b=map(int,input().split())
            price += a*b
        print(price)

# https://www.acmicpc.net/problem/9325