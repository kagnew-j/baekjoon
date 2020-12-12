n = int(input())
n5 = n//5
while True:
    n2 = n - n5*5
    if n2 % 2 == 0:
        print(n5+n2//2)
        break
    else:
        if n5 == 0:
            print(-1)
            break
        else:
            n5 -= 1

# https://www.acmicpc.net/problem/14916