import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque([i+1 for i in range(n)])
idx = len(dq)
while idx != 1:
    dq.popleft()
    dq.append(dq.popleft())
    idx -= 1
print(dq.pop())

###################################################################

import sys
n = int(sys.stdin.readline())
q = [i+1 for i in range(n)]
while len(q) > 1:
    if len(q) % 2:
        q = [q[-1]] + q[1::2]
    else:
        q = q[1::2]
print(q[0])

# https://www.acmicpc.net/problem/2164