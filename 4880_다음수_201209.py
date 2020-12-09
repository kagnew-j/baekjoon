while True:
    a,b,c = map(int,input().split())
    if a == b == c == 0 :
        break
    elif b - a == c - b :
        print("AP", str(c + b - a), sep = " ")
    else :
        print("GP", str(c*(b//a)), sep = " ")

# https://www.acmicpc.net/problem/4880