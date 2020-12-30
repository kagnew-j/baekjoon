import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans = ""
    while n != 1:
        ans += str(n%2)
        n //= 2
    ans += str(1)
    answer = []
    for i in range(len(ans)):
        if ans[i] == '1':
            answer.append(str(i))
    print(" ".join(answer))

# https://www.acmicpc.net/problem/3460