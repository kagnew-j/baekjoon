n = input()
length = len(n)
for i in range(length):
    if n[i:] == n[i:][::-1]:
        print(length + i)
        break

# https://www.acmicpc.net/problem/1254