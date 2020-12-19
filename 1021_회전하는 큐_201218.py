from collections import deque
length, n = map(int,input().split())
targets = list(map(int,input().split()))
dq = deque([i+1 for i in range(length)])
cnt = 0
while targets:
    if targets[0] == dq[0]:
        dq.popleft()
        targets.pop(0)
    else:
        if dq.index(targets[0]) <= len(dq)//2:
            while targets[0] != dq[0]:
                dq.append(dq.popleft())
                cnt += 1
        else:
            while targets[0] != dq[0]:
                dq.appendleft(dq.pop())
                cnt += 1
print(cnt)

# https://www.acmicpc.net/problem/1021