n,k= map(int,input().split())
result = 1
for i in range(n,n-k,-1):
    result *= i
for j in range(1,k+1):
    result //= j
print(result%10007)

# https://www.acmicpc.net/problem/11051
