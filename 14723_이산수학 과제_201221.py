target = int(input())
line = 1
while True:
    if target> line:
        target -= line
        line += 1
    else:
        break
print(line+1-target,target, sep = " ")

# https://www.acmicpc.net/problem/14723