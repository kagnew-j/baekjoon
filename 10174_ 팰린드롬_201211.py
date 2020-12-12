for i in range(int(input())):
    n = input().lower()
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")

# https://www.acmicpc.net/problem/10174