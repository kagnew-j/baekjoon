# Data Input
import sys
input = sys.stdin.readline
n, t = map(int,input().split())
ans = [int(input()) for _ in range(n)]

# sample
n, t = 4, 11
ans = [457, 539, 743, 802]

# binsearch
start, end = 1, max(ans) # min 사용불가 : 하나가 1일 경우 버리고 나머지로 잘라 사용
while start <= end: # = 은 마지막 비교를 마무리하기 위해 사용
    mid = (start + end) // 2
    num = sum([x//mid for x in ans])
    if num >= t:
        start = mid + 1
    else:
        end = mid - 1
# return end
print(end) # end를 return 하는 이유는 start를 마지막으로 end보다 하나 크게 만들어 줬기 때문

# Logic
answer = sum(ans)//t
start = sum([x//answer for x in ans])
while start != t:
    answer -= 1
    start = sum([x//answer for x in ans])
print(answer)
    
# https://www.acmicpc.net/problem/1654


