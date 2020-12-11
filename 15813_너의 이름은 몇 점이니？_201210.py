15813_너의 이름은 몇 점이니？_201210

n = int(input())
target = input()
ans = 0
for i in range(n):
    ans += ord(target[i]) - 64
print(ans)

# https://www.acmicpc.net/problem/18258