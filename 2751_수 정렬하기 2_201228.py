import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    print(i)
    #    sys.stdout.write(str(i)+'\n')
    
# https://www.acmicpc.net/problem/2751