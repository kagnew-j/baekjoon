tot, div = map(int,input().split())
ans = tot
while tot >= div:
    tot //= div
    ans += tot
print(ans)

# https://www.acmicpc.net/problem/17174