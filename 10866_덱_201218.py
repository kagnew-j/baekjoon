import sys
input=sys.stdin.readline
class deque:
    def __init__(self):
        self.items = []
    def push_back(self, x):
        self.items.append(x)
    def push_front(self, x):
        self.items = [x] + self.items
    def pop_front(self):
        if len(self.items) == 0:
            return -1
        else:
            x = self.items[0]
            self.items = self.items[1:]
            return x
    def pop_back(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[0]
    def back(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]
        
answer = deque()
for i in range(int(input().strip())):
    n = list(input().strip().split())
    if n[0] == 'push_front':
        answer.push_front(int(n[1]))
    elif n[0] == 'push_back':
        answer.push_back(int(n[1]))
    elif n[0] == 'pop_front':
        print(answer.pop_front())
    elif n[0] == 'pop_back':
        print(answer.pop_back())
    elif n[0] =='size':
        print(answer.size())
    elif n[0] == 'empty':
        print(answer.empty())
    elif n[0] == 'front':
        print(answer.front())
    elif n[0] == 'back':
        print(answer.back())

# https://www.acmicpc.net/problem/10866