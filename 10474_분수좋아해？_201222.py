while True:
    a,b = map(int,input().split())
    if a == b == 0 :
        break
    print(str(a//b), str(a%b), "/", str(b), sep = " ")

# https://www.acmicpc.net/problem/10474