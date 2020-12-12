from math import gcd as gcd
for _ in range(int(input())):
    li = list(map(int,input().split()))
    ans = 0
    for i in range(1,li[0]):
        for j in range(i+1,li[0]+1):
            ans += gcd(li[i],li[j])
    print(ans)
    
# https://www.acmicpc.net/problem/9613