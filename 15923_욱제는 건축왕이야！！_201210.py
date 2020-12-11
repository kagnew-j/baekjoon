n = int(input())
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    if i == 0 :
        x0, y0 = a, b
        x, y = a, b
    elif i == n-1:
        ans += abs(x-a)+abs(y-b) + abs(x0-a) + abs(y0-b)
    else:
        ans += abs(x-a)+abs(y-b)
        x, y = a, b
print(ans)

# https://www.acmicpc.net/problem/15923