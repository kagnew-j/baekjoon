import math
import collections

def solution(progresses, speeds):
    # 걸리는 시간으로 덱 만들기
    deq = collections.deque()
    for i in range(len(speeds)):
        deq.append(math.ceil((100-progresses[i])/speeds[i])) 
    ans = [] 
    while len(deq) != 0:
        if len(ans) == 0:
            temp = deq.popleft()
            ans.append(1)
        else:
            pop = deq.popleft()
            if temp < pop:
                ans.append(1)
                temp = pop
            else:
                ans[-1] += 1
    return ans