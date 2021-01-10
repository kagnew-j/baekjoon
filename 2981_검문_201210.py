from math import gcd as gcd
import sys
input = sys.stdin.readline
x = 0
temp = []
for i in range(int(input())):
    temp.append(int(input()))
    if i == 0:
        pass
    elif i == 1:
        x = abs(temp[i] - temp[i-1])
    else :
        x = gcd(abs(temp[i]-temp[i-1]),x)
ans = []
for i in range(2,int(x**0.5)+1):
    if x%i == 0:
        ans.append(i)
        ans.append(x//i)
ans.append(x)
ans = sorted(list(set(ans)))
for i in ans:
    print(i, end = ' ')
    
# https://www.acmicpc.net/problem/2981