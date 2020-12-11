import sys
n = int(sys.stdin.readline())
a = 0
for i in range(1,n+1):
    while i % 5 == 0:
        i //= 5
        a += 1
print(a)

# https://www.acmicpc.net/problem/1676