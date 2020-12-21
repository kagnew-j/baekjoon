n = int(input())
li = list(map(int,input().split()))
ans = []
for i in range(n):
    ans.append(li[i]*(i+1)-sum(ans))
for ele in ans:
    print(ele, end = " ")
    
# https://www.acmicpc.net/problem/10539