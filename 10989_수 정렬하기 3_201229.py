import sys
input = sys.stdin.readline

target = {}
for _ in range(int(input())):
    n = int(input())
    target[n] = target.get(n,0) + 1

ans = sorted(target.items(), key = lambda x : x[0])
for ele in ans:
    for _ in range(ele[1]):
        print(ele[0])
        #sys.stdout.write(str(ele[0])+'\n') # 조금 더 빠름
        
# https://www.acmicpc.net/problem/10989