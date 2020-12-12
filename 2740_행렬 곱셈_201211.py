import sys
input = sys.stdin.readline
a = []
a1,a2 = map(int,input().split())
for _ in range(a1):
    a.append(list(map(int,input().split())))
b = []
b1,b2 = map(int,input().split())
for _ in range(b1):
    b.append(list(map(int,input().split())))

c = [[0 for i in range(b2)] for _ in range(a1)]

for i in range(a1):
    for j in range(b2):
        for k in range(a2):
            c[i][j] += a[i][k]*b[k][j]
for i in c:
    for j in i:
        print(j, end = ' ')
    print()        

# https://www.acmicpc.net/problem/2740