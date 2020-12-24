def stack_list(x):
    """
    임시로 비워둠
    """
    cnt, stack, output = 1, [], []
    for ele in x:
        while cnt <= ele:
            stack.append(cnt)
            output.append("+")
            cnt += 1
        if stack.pop() != ele:
            return "NO"
        else:
            output.append("-")
    return "\n".join(output)

import sys
input = sys.stdin.readline
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))
print(stack_list(x))

# https://www.acmicpc.net/problem/1874