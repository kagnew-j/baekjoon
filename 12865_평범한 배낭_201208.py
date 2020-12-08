import sys
input = sys.stdin.readline
n,w = map(int,input().split())
obj = []
for _ in range(n):
    a,b = map(int,input().split())
    obj.append((a,b))
bag = [0 for _ in range(w+1)]
for i in range(n):
    for j in range(w,0,-1):
        if obj[i][0] <= j:
            bag[j] = max(bag[j], bag[j-obj[i][0]] + obj[i][1])
print(max(bag))
# https://www.acmicpc.net/submit/12865/24262936