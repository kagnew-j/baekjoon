import sys
input=sys.stdin.readline
class queue:
    def __init__(self):
        self.items = []
        self.idx = 0
        self.cnt = 0
    def push(self, x):
        self.items.append(x)
        self.cnt += 1
    def pop(self):
        if self.cnt - self.idx == 0:
            return -1
        else:
            x = self.items[self.idx]
            self.idx += 1
            return x
    def size(self):
        return self.cnt - self.idx
    def empty(self):
        if self.cnt - self.idx == 0:
            return 1
        else:
            return 0
    def front(self):
        if self.cnt - self.idx == 0:
            return -1
        else:
            return self.items[self.idx]
    def back(self):
        if self.cnt - self.idx == 0:
            return -1
        else:
            return self.items[-1]
        
answer = queue()
for i in range(int(input().strip())):
    n = input().strip()
    if n[:4] == 'push':
        a,b = n.split()
        answer.push(int(b))
    elif n == 'pop':
        print(answer.pop())
    elif n =='size':
        print(answer.size())
    elif n == 'empty':
        print(answer.empty())
    elif n == 'front':
        print(answer.front())
    elif n == 'back':
        print(answer.back())

# https://www.acmicpc.net/problem/18258