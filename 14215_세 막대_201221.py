li = list(map(int,input().split()))
c = max(li)
ab = sum(li) - c
if c >= ab:
    print(2*ab-1)
else:
    print(ab+c)
    
# https://www.acmicpc.net/problem/14215    