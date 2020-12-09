n, m = map(int,input().split())
li = list(map(int,input().split()))
ans = 1
for ele in li:
    ans = ((ans%m)*(ele%m))%m
print(ans)

# https://www.acmicpc.net/problem/15818