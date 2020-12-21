n,x,k = map(int,input().split())
shell = [0]*(n+1)
shell[x] = 1
for _ in range(k):
    a,b = map(int,input().split())
    shell[a], shell[b] = shell[b], shell[a]
print(shell.index(1))

# https://www.acmicpc.net/problem/20361