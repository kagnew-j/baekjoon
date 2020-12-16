while True:
    n = int(input())
    if n == 0:
        break
    elements = iter(map(int,input().split()))
    m, j = 0, 0
    for ele in elements:
        if ele == 0:
            m += 1
        else:
            j += 1
    print("Mary won {} times and John won {} times".format(m, j))

# https://www.acmicpc.net/problem/5751