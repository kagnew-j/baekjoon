def num(n,target):
    answer = 0
    while n != 0:
        n //= target
        answer += n
    return answer

n,m = map(int,input().split())
if m == 0:
    print(0)
else:
    print(min(num(n,2)-num(m,2)-num(n-m,2),num(n,5)-num(m,5)-num(n-m,5)))
    
# https://www.acmicpc.net/problem/2004