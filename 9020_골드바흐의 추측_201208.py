num = []
m = 0
for _ in range(int(input())):
    n = int(input())
    num.append(n)
    m = max(m,n)
# sieve structure
if m < 2:
    sieve = [False]*(m+1)
else:
    sieve = [False, False] + [True]*(m-1) 
# sieve checker game
for i in range(2,m+1):
    if sieve[i]:
        for j in range(2*i,m+1,i):
            sieve[j] = False
# answer
for ele in num:
    temp = []
    for i in range(2,ele//2+1):
        if sieve[i]:
            if sieve[ele-i]:
                temp.append((i,ele-i))
    print(temp[-1][0], temp[-1][1], sep = " ")

# https://www.acmicpc.net/problem/9020