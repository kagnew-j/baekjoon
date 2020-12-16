def calculate(a,b,c):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    elif c == "*":
        return a*b
    elif c == '/':
        return a//b
ans = 0
idx = 0
while True:
    n = input()
    if n == "=":
        print(ans)
        break
    if idx == 0:
        ans = int(n)
        idx = 1
    elif idx == 1:
        temp = n
        idx = 2
    elif idx == 2:
        ans = calculate(ans,int(n),temp)
        idx = 1

# https://www.acmicpc.net/problem/5613