def elevate(x):
    if x % 2 != 0:
        return x//2 + 1
    else:
        return x//2

def solution(n,a,b):
    temp = 0
    while a != b:
        temp += 1
        a = elevate(a)
        b = elevate(b)
        if a == b:
            break
    return temp

# https://programmers.co.kr/learn/courses/30/lessons/12985