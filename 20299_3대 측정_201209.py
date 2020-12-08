import sys
n,k,l = map(int,sys.stdin.readline().split())
answer = 0
ans = []
for i in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    flag = True
    for i in li:
        if i < l:
            flag = False
            break
    if flag:
        temp = sum(li)
        if temp >= k:
            ans += li
            answer += 1
print(answer)
print(*ans)

# https://www.acmicpc.net/problem/20299