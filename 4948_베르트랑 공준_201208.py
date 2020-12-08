nums = []
m = 0
while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)
    m = max(m,n)
# sieve structure
if m < 2:
    sieve = [False]*(2*m+1)
else:
    sieve = [False, False] + [True]*(2*m-1) 
# sieve checker game
for i in range(2,2*m+1):
    if sieve[i]:
        for j in range(2*i,2*m+1,i):
            sieve[j] = False
# print answer
for j in nums:
    print(sum(sieve[j+1:2*j+1]))
# https://www.acmicpc.net/problem/4948