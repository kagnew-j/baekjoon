n = int(input())-1
target = list(input())
for i in range(n//2+1):
    if n-i>i:
        if target[i] =="?":
            if target[n-i] == "?":
                target[i], target[n-i] = 'a','a'
            else:
                target[i] = target[n-i]
        else:
            if target[n-i] == "?":
                target[n-i] = target[i]
            else:
                pass
    elif n-i == i:
        if target[i] == "?":
            target[i] = 'a'
    else:
        pass
print("".join(target))

# https://www.acmicpc.net/problem/17502