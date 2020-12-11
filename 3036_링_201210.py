import math
import sys
input = sys.stdin.readline
n = int(input())
ans = list(map(int,input().split()))
for i in range(1,n):
    gcd = math.gcd(ans[0],ans[i])
    print(str(ans[0]//gcd)+"/"+str(ans[i]//gcd))

# https://www.acmicpc.net/problem/3036