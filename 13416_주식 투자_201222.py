for i in range(int(input())):
    ans = 0
    for j in range(int(input())):
        ans += max(0,max(list(map(int,input().split()))))
    print(ans)

# https://www.acmicpc.net/problem/13416