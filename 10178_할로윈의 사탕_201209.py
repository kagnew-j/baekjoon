for i in range(int(input())):
    a,b=map(int,input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(a//b,a%b))

# https://www.acmicpc.net/problem/10178